"""Syynk lyrics in 3D - builds a Blender scene from a Syynk JSON export.

Every lyric line becomes extruded 3D text, one object per word. A line appears
dim, each word lights up as it is sung, and the line fades out at its own end.
Backing vocals appear under the lead line in their own colour.

Run it with Blender (no other install needed; Blender brings its own Python):

    blender -b --factory-startup --python syynk_blender_lyrics.py -- my-song.json my-song.mp3 --save my-song.blend
    blender -b --factory-startup --python syynk_blender_lyrics.py -- my-song.json --still 60 520
    blender -b --factory-startup --python syynk_blender_lyrics.py -- my-song.json --render out/

    --save FILE      save a .blend you can open and play (Space) with the song in sync
    --still F ...    render single frames to PNG next to the JSON file
    --render DIR     render the whole song as a PNG sequence into DIR

The song file is optional. It is only used by --save, to put the audio on the
timeline. Export the JSON from Syynk with word timing included.
"""
import json
import math
import os
import sys

import bpy

# --- Settings ----------------------------------------------------------------

FONT            = None         # path to a .ttf/.otf file, or None for Blender's built-in font
LEAD_COLOR      = "#F4EFE6"    # sung lead words (hex, as in any design tool)
BACKING_COLOR   = "#F2C14E"    # backing vocals / responses
BACKGROUND      = "#101014"
TRANSPARENT     = False        # True: see-through background, to lay the lyrics over video
UNSUNG_LEVEL    = 0.15         # brightness of a word before it is sung (0-1)
LINE_WIDTH      = 0.7          # widest a line may get, as a share of the frame width
TEXT_SIZE       = 0.6          # largest text height, in scene units (short lines stop here)
DEPTH           = 0.06         # extrusion depth, in scene units
FPS             = 30
WIDTH, HEIGHT   = 1920, 1080   # 1080 x 1920 for vertical video
FADE_FRAMES     = 5            # frames to fade a line in and out
ENGINE          = "EEVEE"      # "EEVEE" (fast) or "CYCLES" (slower, more realistic)

# --- End of settings ----------------------------------------------------------

CAMERA_DISTANCE = 10.0
LENS, SENSOR = 50.0, 36.0


def linear(hexcode):
    """Blender colours are linear: convert an sRGB hex colour, or it washes out."""
    c = [int(hexcode.lstrip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in c)


def frame(seconds):
    return round(seconds * FPS)


def load_lines(path):
    data = json.load(open(path, encoding="utf-8"))
    segments = data["segments"] if isinstance(data, dict) else data
    lines = []
    for seg in segments:
        kind = seg.get("kind", "lyric")
        words = seg.get("words") or []
        if kind not in ("lyric", "backing") or not words:
            continue            # section labels and instrumental breaks have no words to show
        lines.append({"kind": kind, "start": seg["startTime"], "end": seg["endTime"],
                      "words": [(w["word"], w["startTime"], w["endTime"]) for w in words]})
    if not lines:
        sys.exit("No timed words found. Export the JSON from Syynk with word timing included.")
    return lines


def new_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    engines = [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items]
    if ENGINE == "CYCLES":
        sc.render.engine = "CYCLES"
    else:
        sc.render.engine = next(e for e in ("BLENDER_EEVEE", "BLENDER_EEVEE_NEXT") if e in engines)
    sc.render.resolution_x, sc.render.resolution_y = WIDTH, HEIGHT
    sc.render.fps = FPS
    # Standard does no extra conversion besides the display's. In a test with
    # Blender 5.2's factory settings the view transform was AgX, and gold came out tan.
    sc.view_settings.view_transform = "Standard"
    sc.render.image_settings.file_format = "PNG"
    if TRANSPARENT:
        sc.render.film_transparent = True
        sc.render.image_settings.color_mode = "RGBA"
    world = bpy.data.worlds.new("background")
    if world.node_tree is None:
        world.use_nodes = True   # Blender 5 gives new worlds nodes already
    world.node_tree.nodes["Background"].inputs["Color"].default_value = (*linear(BACKGROUND), 1)
    sc.world = world
    # Every key below is linear, so a word fills in evenly rather than easing.
    bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"
    return sc


def add_camera_and_light(sc):
    cam_data = bpy.data.cameras.new("camera")
    cam_data.lens, cam_data.sensor_width = LENS, SENSOR
    cam = bpy.data.objects.new("camera", cam_data)
    cam.location = (0.0, -CAMERA_DISTANCE, 0.0)
    cam.rotation_euler = (math.radians(90), 0.0, 0.0)
    sc.collection.objects.link(cam)
    sc.camera = cam
    light_data = bpy.data.lights.new("key", "AREA")
    light_data.shape = "DISK"   # a square area light draws a hard edge through any haze
    light_data.size, light_data.energy = 6.0, 400.0
    light = bpy.data.objects.new("key", light_data)
    light.location = (0.0, -6.0, 4.0)
    light.rotation_euler = (math.radians(55), 0.0, 0.0)
    sc.collection.objects.link(light)


def word_material(name, color):
    m = bpy.data.materials.new(name)
    if m.node_tree is None:
        m.use_nodes = True       # Blender 5 gives new materials nodes already
    m.surface_render_method = "BLENDED"   # smooth fades
    m.use_transparency_overlap = False    # extruded text would sort against its own faces
    m.use_backface_culling = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Roughness"].default_value = 0.45
    bsdf.inputs["Emission Color"].default_value = (*color, 1)
    return m, bsdf


def key(socket, table):
    for f, value in sorted(table.items()):
        socket.default_value = value
        socket.keyframe_insert("default_value", frame=f)


def build_line(sc, line, index, font, frame_width):
    color = linear(BACKING_COLOR if line["kind"] == "backing" else LEAD_COLOR)
    objs = []
    for text, _, _ in line["words"]:
        curve = bpy.data.curves.new(f"w{index}_{text}", "FONT")
        curve.body, curve.size = text, 1.0
        if font:
            curve.font = font
        curve.extrude, curve.bevel_depth = DEPTH, DEPTH * 0.15
        curve.align_x, curve.align_y = "LEFT", "CENTER"
        ob = bpy.data.objects.new(curve.name, curve)
        ob.rotation_euler = (math.radians(90), 0.0, 0.0)   # face the camera
        sc.collection.objects.link(ob)
        objs.append(ob)

    # Lay the words out at size 1, then scale the line to fit.
    bpy.context.view_layer.update()
    space = 0.25
    widths = [o.dimensions.x for o in objs]
    total = sum(widths) + space * (len(objs) - 1)
    size = min(TEXT_SIZE, LINE_WIDTH * frame_width / total)
    if line["kind"] == "backing":
        size *= 0.7
    z = -1.1 * TEXT_SIZE if line["kind"] == "backing" else 0.0

    fa, fb = frame(line["start"]), frame(line["end"])
    x = -size * total / 2
    for ob, (text, ws, we), width in zip(objs, line["words"], widths):
        ob.data.size = size
        ob.location = (x, 0.0, z)
        x += size * (width + space)
        m, bsdf = word_material(ob.name, color)
        ob.data.materials.append(m)
        lit0, lit1 = max(fa, frame(ws)), max(fa + 1, frame(ws) + 3)
        out0, out1 = max(fa + FADE_FRAMES, fb - FADE_FRAMES), fb
        dim = tuple(c * UNSUNG_LEVEL for c in color) + (1.0,)
        full = color + (1.0,)
        # The unsung state is solid and dark, not transparent: extruded text at low
        # opacity shows its edges and looks broken. Opacity only fades whole lines.
        key(bsdf.inputs["Base Color"], {fa - FADE_FRAMES: dim, lit0: dim, lit1: full})
        key(bsdf.inputs["Emission Strength"], {fa - FADE_FRAMES: 0.0, lit0: 0.0, lit1: 1.0,
                                               lit1 + 8: 0.6, out0: 0.6, out1: 0.0})
        key(bsdf.inputs["Alpha"], {fa - FADE_FRAMES: 0.0, fa: 1.0, out0: 1.0, out1: 0.0})
        # Keep the word out of the render entirely outside its line.
        for f, hidden in ((fa - FADE_FRAMES - 1, True), (fa - FADE_FRAMES, False), (out1 + 1, True)):
            ob.hide_render = ob.hide_viewport = hidden
            ob.keyframe_insert("hide_render", frame=f)
            ob.keyframe_insert("hide_viewport", frame=f)


def build(json_path):
    lines = load_lines(json_path)
    sc = new_scene()
    add_camera_and_light(sc)
    font = bpy.data.fonts.load(FONT) if FONT else None
    frame_width = 2 * CAMERA_DISTANCE * (SENSOR / 2) / LENS
    if HEIGHT > WIDTH:
        frame_width *= WIDTH / HEIGHT     # the sensor fits the wider side
    for i, line in enumerate(lines):
        build_line(sc, line, i, font, frame_width)
    sc.frame_start = 0
    sc.frame_end = frame(max(line["end"] for line in lines)) + FPS
    print(f"Built {len(lines)} lines ({sum(len(l['words']) for l in lines)} words), "
          f"frames {sc.frame_start}-{sc.frame_end} at {FPS} fps.")
    return sc


def main(argv):
    if not argv or argv[0].startswith("--"):
        sys.exit(__doc__)
    json_path = os.path.abspath(argv[0])
    audio = argv[1] if len(argv) > 1 and not argv[1].startswith("--") else None
    for path in filter(None, (json_path, audio)):
        if not os.path.isfile(path):
            sys.exit(f"Can't find {path}. Run this from the folder that holds it, or give its full path.")
    sc = build(json_path)
    base = os.path.splitext(json_path)[0]
    if "--still" in argv:
        for f in argv[argv.index("--still") + 1:]:
            if f.startswith("--"):
                break
            sc.frame_set(int(f))
            sc.render.filepath = f"{base}_{int(f):05d}.png"
            bpy.ops.render.render(write_still=True)
            print("Rendered", sc.render.filepath)
    if "--render" in argv:
        out = argv[argv.index("--render") + 1]
        sc.render.filepath = os.path.join(os.path.abspath(out), "frame_")
        bpy.ops.render.render(animation=True)
        print("Rendered frames to", out)
    if "--save" in argv:
        if audio:
            # Song frames = scene frames, played in sync.
            sc.sequence_editor_create().strips.new_sound("song", os.path.abspath(audio), 1, 0)
            sc.sync_mode = "AUDIO_SYNC"
        path = os.path.abspath(argv[argv.index("--save") + 1])
        bpy.ops.wm.save_as_mainfile(filepath=path)
        print("Saved", path)


if __name__ == "__main__":
    main(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
