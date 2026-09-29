# `skills/`

Every skill in this catalog lives here as one directory. Adding a skill is a directory plus an
entry in [`../.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json).

## Layout

```
skills/
└── <skill-name>/
    ├── SKILL.md              # the skill — YAML frontmatter + body
    ├── references/
    │   └── sources.json      # provenance: sources + claim-level citations
    └── templates/            # optional — reusable structures the skill emits
```

## Naming

**Bare, descriptive, unbranded** — `ddex-delivery`, not `royalti-ddex-delivery`. These read as
industry knowledge, and the catalog name carries whatever namespacing is needed.

The trade-off is deliberate and worth knowing: a generic directory name can collide with another
skill claiming the same name in a user's skill directory. We took that over branding a reference
work.

## What every skill must carry

Both gates are merge blockers. Neither is optional for a new skill.

1. **Frontmatter** — `name` and `description`. The description is what a tool matches against to
   decide whether to load the skill, so it should name the situations the skill is for, not just
   its subject.
2. **`references/sources.json`** — provenance in the shape described in
   [`../ACCURACY-GATE.md`](../ACCURACY-GATE.md), including the `claims[]` array. Claim-level, not
   document-level: a list of authoritative URLs at the bottom of a skill proves nothing about any
   individual sentence.
3. **A verification stamp** — `Verified against primary sources: YYYY-MM-DD`. Specifications
   move. An old stamp is honest; an absent one is not.
4. **A scrub pass** — `../scripts/scrub-scan.sh skills/<skill-name>`, then the four rules in
   [`../SCRUB-CHECKLIST.md`](../SCRUB-CHECKLIST.md) read by a human. The scan is a worklist, not
   a verdict: a clean run is not a pass.

## Scope of this catalog

Process and format knowledge in music rights and distribution — how a specification works, what
a field means, where a submission goes.

**Not** product documentation, **not** legal or financial advice, and **not** a replacement for
the specifications themselves. The practical limit is citability: a subject with no primary
sources we can point at cannot be published here under the accuracy gate, however well we know it.

## Published

- `royalti-app` — task router for the Royalti.io app: 46 help articles regrouped by task. Link-checked 2026-08-23.
- `ddex-delivery` — problem router: 209 delivery failure modes → the DDEX guidance article that answers each. Link-checked 2026-08-23.
- `ddex-sources` — primary-source index for music delivery. Link-checked 2026-08-21.
- `cwr-registration` — the MusicMark route to ASCAP, BMI and SOCAN. Verified 2026-08-21.
- `syynk-blender-lyrics` — Syynk.to lyrics JSON → 3D lyric text in Blender, with its script. Verified 2026-09-29.

## In preparation

Nothing currently. Skills are added when there is material we can cite; see
[`../ACCURACY-GATE.md`](../ACCURACY-GATE.md). **A skill appears in the manifest when it has
passed both gates, not when its directory exists.**
