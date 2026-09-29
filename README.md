# Royalti Skills

**Free, cited reference skills for the parts of the music business that are documented badly
or not at all** — DDEX delivery, publishing registration, rights administration.

If you deliver releases to DSPs, register works with a PRO, or administer rights for a
catalogue, this catalog is written for you. Each skill is a working reference you can install
into an AI coding tool and ask questions of — not marketing, not a whitepaper.

Every normative claim in these skills cites a primary source. Where we could not cite
something, we removed it rather than hedging it. See [`ACCURACY-GATE.md`](ACCURACY-GATE.md).

## Why we built this

We build [Royalti.io](https://royalti.io), a rights and royalty platform, which means we spend
our days inside DDEX message profiles, CWR record types and PRO submission routes. Almost none
of that is documented publicly in a form a practitioner can actually use — the specifications
are dense and paywalled by expertise, and the accessible material is usually a vendor's
marketing page. These skills are the reference we wanted when we started. They cost us little
to publish and they are useless to us kept private.

## The catalog

| Skill | What it covers | License |
|---|---|---|
| [`royalti-app`](skills/royalti-app/) | Task router for the Royalti.io app — 46 help articles regrouped by what you are trying to do. | Apache-2.0 |
| [`ddex-delivery`](skills/ddex-delivery/) | Problem router for DDEX delivery — 209 real failure modes mapped to the DDEX guidance article that answers each. | Apache-2.0 |
| [`ddex-sources`](skills/ddex-sources/) | Primary-source index for music delivery — the ten DDEX standards, plus DSP, aggregator and regional-platform documentation. Link-checked. | Apache-2.0 |
| [`cwr-registration`](skills/cwr-registration/) | Registering works with PROs via CWR — the MusicMark route to ASCAP, BMI and SOCAN: test phase, file naming, SFTP, acknowledgment codes, work IDs. | Apache-2.0 |
| [`syynk-blender-lyrics`](skills/syynk-blender-lyrics/) | Turn a [Syynk.to](https://syynk.to) lyrics JSON export into 3D lyric text in Blender, lit word by word — with the script that builds, previews and renders it. | Apache-2.0 |
| [`royalti-api`](https://github.com/Royalti-io/royalti-api-skill) | Royalti.io REST API v2.6 — auth, CRUD, pagination, webhooks, WebSocket events | MIT |

_More skills as we find material we can cite. [Suggest one](https://github.com/Royalti-io/royalti-skills/issues)._

**This catalog is mixed-license.** Skills in this repository are Apache-2.0. `royalti-api`
lives in its own repository under MIT and is listed here rather than absorbed. The table above
states the license for every entry.

## Install

### Claude Code (plugin marketplace)

```bash
/plugin marketplace add Royalti-io/royalti-skills
/plugin install <skill-name>
```

### Any Agent Skills compatible tool

```bash
npx skills add royalti-io/royalti-skills
```

Works with Claude Code, Cursor, OpenAI Codex CLI, and anything else that reads the
[Agent Skills](https://agentskills.io) standard.

Once installed, a skill activates automatically when your conversation involves its subject.

### Which path installs what

The two paths do not cover the same entries, so pick by what you want:

| | Plugin marketplace | `npx skills add` |
|---|---|---|
| `royalti-app` | ✅ | ✅ |
| `ddex-delivery` | ✅ | ✅ |
| `ddex-sources` | ✅ | ✅ |
| `cwr-registration` | ✅ | ✅ |
| `syynk-blender-lyrics` | ✅ | ✅ |
| `royalti-api` | ✅ | ❌ — install it [from its own repo](https://github.com/Royalti-io/royalti-api-skill) |

`royalti-api` lives in a separate repository. The marketplace manifest can point at it; the
skills CLI reads this repository's `skills/` directory and so does not pick it up. Verified by
installing, not assumed.

## What these skills are not

- **Not a product manual.** Except for `royalti-api`, nothing here describes what Royalti
  supports. These are industry references; where a skill covers ground broader than any
  product's actual support, it says so.
- **Not legal or financial advice.** Rights administration has legal consequences. These skills
  describe formats and processes; they do not tell you what to agree to.
- **Not a substitute for the specifications.** They cite the specifications. Read those when a
  decision matters.

## Accuracy

Two documents govern everything published here, and both are merge blockers:

- **[`ACCURACY-GATE.md`](ACCURACY-GATE.md)** — every normative claim cites a primary source at
  the claim level, and survives an adversarial pass that tries to refute it. Uncitable claims
  are deleted, not softened.
- **[`SCRUB-CHECKLIST.md`](SCRUB-CHECKLIST.md)** — no internal operations detail, no
  partner-confidential material, no unattributed claims, no capability claims.

Each skill carries a dated `Verified against primary sources` stamp. Specifications move; an
old stamp is honest, an absent one is not.

**Found something wrong?** [Open an issue](https://github.com/Royalti-io/royalti-skills/issues).
Corrections to published claims are the most useful thing you can send us — see
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Apache-2.0 for this repository — see [`LICENSE`](LICENSE). Individual catalog entries hosted
elsewhere carry their own license, stated in the table above.

Maintained by [Royalti.io](https://royalti.io).
