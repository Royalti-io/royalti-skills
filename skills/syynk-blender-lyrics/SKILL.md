---
name: syynk-blender-lyrics
description: Turn a Syynk lyrics JSON export into 3D lyric text in Blender, with each word lit as it is sung. Use when someone has a .json lyrics export from Syynk.to (exported with word-level timing) and wants a 3D lyric video, lyric renders or a .blend file, or wants to restyle, preview or render those lyrics in Blender.
---

# Syynk lyrics in 3D, with Blender

**What this covers:** running the bundled script, `scripts/syynk_blender_lyrics.py`, on a lyrics
export from [Syynk.to](https://syynk.to). The script builds a Blender scene:
- every word is extruded 3D text;
- a line appears dim, and each word lights as it is sung;
- each line fades at its own end;
- backing-vocal lines sit underneath in their own colour.

**What it does not cover:** Blender in general, or lyric timing itself. The timing comes from
the export; the script does not re-time it. It rounds times to whole frames and adds short
fades around each line.

**Scope:** this skill is tied to one tool's export. It is not an industry reference like the
rest of this catalog. It describes a script that is published today: the same file is
downloadable from [syynk.to/downloads/syynk_blender_lyrics.py](https://syynk.to/downloads/syynk_blender_lyrics.py).

**Verified against primary sources: 2026-09-29.**
**Reviewed and signed off: 2026-09-29** — Chinedum Okerengwor, Royalti.io. Scrub checklist and
accuracy gate both PASS; see [`references/sources.json`](references/sources.json) for the
per-claim record. Where this page reports something we observed rather than something a source
states, it says "in our test".

---

## 1. Check the export

The script reads the export's `segments` list. It draws a segment when its `kind` is `lyric` or
`backing` (a segment with no `kind` counts as `lyric`) and its `words` list is not empty. It
reads each drawn segment's `startTime` and `endTime`, and each word's `word`, `startTime` and
`endTime`, in seconds. Segments of any other kind are skipped.

If no `lyric` or `backing` segment has words, the script stops with:

```text
No timed words found. Export the JSON from Syynk with word timing included.
```

Word-level timing is an option when exporting JSON from Syynk's LyricSync editor, and it is
**off by default**. If the
export has no words, ask the user to export again with **Include word-level timing** ticked.

## 2. Set it up

Copy `scripts/syynk_blender_lyrics.py` next to the user's JSON file. Apply what they asked for
by editing **only the settings block** at the top, between `# --- Settings` and
`# --- End of settings`:

| Setting | What it controls |
| --- | --- |
| `FONT` | Path to a font file. `None` uses Blender's built-in font. |
| `LEAD_COLOR` | Hex colour of the sung lead lines. Default `#F4EFE6`. |
| `BACKING_COLOR` | Hex colour of backing vocals and responses. Default `#F2C14E`. |
| `BACKGROUND` | Hex background colour. |
| `TRANSPARENT` | `True` renders a transparent background. |
| `UNSUNG_LEVEL` | Brightness of a word before it is sung, 0 to 1. |
| `LINE_WIDTH`, `TEXT_SIZE`, `DEPTH` | Layout and letter depth. |
| `FADE_FRAMES` | Frames to fade a line in and out. |
| `FPS` | Frame rate. Match the video you are making. |
| `WIDTH`, `HEIGHT` | Frame size in pixels. For example, 1080 × 1920 for vertical. |
| `ENGINE` | `"EEVEE"` or `"CYCLES"`. |

Give colours as six-digit hex codes (`#RRGGBB`). Blender primarily works with scene-linear
colours for materials, and the working space defaults to Linear Rec.709. The script applies
the sRGB-to-linear transfer function to each hex colour itself and starts from factory settings
without changing the working space, so never convert colours by hand.

The script also sets the scene's view transform to **Standard**, which does no extra conversion
besides the one for the display. Leave it there. AgX, another view transform, is a tone-mapping
transform. In our test, with Blender 5.2's factory settings, the view transform was AgX, and a
requested gold (`#F2C14E`) rendered as a muted tan.

The camera does not move and faces the text, and none of the settings move or aim the camera,
or add a set. If the user wants a camera move or a 3D set, build it on the saved `.blend` file.

## 3. Preview before rendering

If you can run commands, run Blender headless. `-b` runs it in the background, which is often
used for rendering without the interface. `--factory-startup` skips reading the user's
`startup.blend`, and `--python` runs a script file. Blender stops processing options at `--` and
leaves the arguments after it unchanged in Python's `sys.argv`; the script reads what follows
the `--`.

```bash
blender -b --factory-startup --python syynk_blender_lyrics.py -- song.json --still 60 545
```

`--still` renders the listed frames to PNG files next to the JSON, named after the JSON file with the frame number padded to five
digits: `song_00060.png`. The scene starts at frame 0, so a frame number is seconds × `FPS`. Pick moments inside lines: a word's `startTime` plus a little.
If the export has `backing` segments, include a frame where a backing line overlaps a lead line.

`--still`, `--render` and `--save` can be combined in one run. The song file, when given, is
used only by `--save`.

Look at the images before going further:
- the sung words are bright and the rest are dim;
- nothing runs off the edge;
- the colours are the ones asked for.

## 4. Save or render

- **Watch it with the song:**
  `blender -b --factory-startup --python syynk_blender_lyrics.py -- song.json song.mp3 --save song.blend`
  saves a `.blend` file. When the song file is given as the second argument, as here, it also
  puts the song on the timeline and sets playback to sync to the audio, so the user can open the
  `.blend` file and play it back with the song. The file links to the song by its full path, so
  keep the song where it is. The timeline ends one second after the last line.
- **Render every frame:**
  `blender -b --factory-startup --python syynk_blender_lyrics.py -- song.json --render frames`
  writes a numbered PNG sequence. Tell the user how long it may take: in our test, EEVEE took about
  2 seconds a frame on an RTX 2070 Max-Q laptop GPU. At that rate, a three-minute song at 30 fps
  would take roughly three hours; that figure is an estimate, not a measurement.

If you cannot run commands, for example in a chat app, give the user the edited script and
these commands.

## Messages the script prints

- `No timed words found. Export the JSON from Syynk with word timing included.` No `lyric` or
  `backing` segment in the export has words.
- `Can't find <path>. Run this from the folder that holds it, or give its full path.` The JSON
  or song file passed to the script does not exist.
- `Built N lines (M words), frames A-B at FPS fps.` Printed once the scene is built, before
  any render or save.

## Sources

Every claim above is traced to one of these, with the location, in
[`references/sources.json`](references/sources.json).

| Source | Authoritative for |
| --- | --- |
| [`scripts/syynk_blender_lyrics.py`](scripts/syynk_blender_lyrics.py) | What the script reads, builds, sets and prints |
| [Blender Manual — Command Line Arguments](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html) | `-b`, `--factory-startup`, `--python`, and arguments after `--` |
| [Blender Manual — Color Spaces](https://docs.blender.org/manual/en/latest/render/color_management/color_spaces.html) | Scene-linear colour |
| [Blender Manual — Displays & Views](https://docs.blender.org/manual/en/latest/render/color_management/displays_views.html) | The Standard and AgX view transforms |
| [Syynk — Put your lyrics in 3D with Blender](https://syynk.to/docs/guides/blender-lyrics) | The export option and its default |

**Found something wrong?** [Open an issue](https://github.com/Royalti-io/royalti-skills/issues).
