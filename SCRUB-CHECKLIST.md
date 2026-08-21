
# Scrub checklist

Every skill in this repo passes this checklist before it goes public, and again on every
pull request that touches it. It is a **merge blocker**, not a guideline.

## Why this exists

The people who read this material are rights administrators, label operations staff,
distributors and publishers — the people who would notice. A wrong or leaky line here is not
a GitHub issue, it is a credibility event with the exact audience the work is meant to reach.
That asymmetry is the whole reason the gate runs before the first publish rather than after
the first complaint.

## The four rules

### 1. No internal operations detail

Skills describe **how the industry works**, never how one company runs.

Cut on sight:

- Repository paths, service names, module paths, file layouts belonging to a private codebase
- Internal API endpoints, database table or column names, queue or job names
- Runbook steps that only make sense with access to a private system
- Tenant, workspace, account or user identifiers, in any format
- References to internal documents a reader cannot open
- Environment, deployment or credential-location detail — *including statements about where a
  credential is **not** stored*. A sentence that maps the credential landscape is a leak even
  when it discloses nothing directly.

The test: **would this line still make sense, and still be useful, to a reader who has never
had access to our systems?** If it needs insider context to parse, it is internal detail.

### 2. No partner-confidential or roster material

This is the rule that most often means *delete the source*, not *edit it*.

Cut on sight:

- Named artists, releases or catalogue tied to a specific commercial relationship
- Contract terms, rates, commissions, splits or deal structure with any partner
- Party, aggregator or account identifiers that tie an organisation to a specific service
- Anything describing a partner's non-public behaviour, backoffice or support process
- Screenshots or transcripts of a partner-operated system

Rewording does not fix this class. Roster identity and account identity are the facts
themselves — remove them, or drop the source.

**If what remains after this rule is applied is thin, ship it thin or ship nothing.** Padding a
scrubbed remainder back to a respectable length reintroduces exactly the uncited assertion the
next rule forbids.

### 3. No unattributed normative claim

Every claim about how a specification, format, standard or submission route *works* carries a
citation to a primary source. See `ACCURACY-GATE.md` for what counts as primary, how citations
are recorded, and the verification pass.

The rule in one line: **an uncitable normative claim is deleted, not softened.** "Generally,"
"typically," and "in most cases" are not citations. A hedge is an uncited claim wearing a hat.

Non-normative material — worked examples, structural guidance, "here is a sensible order to do
this in" — does not need a citation, but must not be phrased as though it were a specification
requirement.

### 4. No product-capability claim that isn't shipped

Skills in this repo are industry knowledge. They are not marketing surface.

- Do not state or imply that any product supports something it does not currently support and
  ship. Not "planned," not "on the roadmap," not "supported in principle."
- Feature-comparison tables that put a product in a column against a specification are a
  capability claim by construction. **Remove the column.** If the comparison is the point, the
  skill is in the wrong repo.
- Where a skill covers ground broader than any product's actual support, say so explicitly in
  the skill text. An accurate sentence that the reader never sees does not do the job — the
  separating line must be *in the document*, not merely true.

## Mechanical pass

Run before every publish and on every PR touching a skill. It catches the easy half; the four
rules above catch the half that matters.

```bash
# from the repo root
./scripts/scrub-scan.sh skills/<skill-name>
```

The script greps for the marker classes below and prints file:line for review. **A hit is not
automatically a failure and a clean run is not a pass** — it is a worklist. Rules 1–4 are read
by a human either way.

| Marker class | What it catches |
|---|---|
| Private-org and product names | Rule 1, Rule 4 — internal framing, capability claims |
| Partner and service names | Rule 2 — relationship disclosure |
| Identifier shapes (UUIDs, numeric tenant/account IDs, party/aggregator ID formats) | Rule 1, Rule 2 |
| Internal path shapes (`src/`, repo-name prefixes, dotfile directories) | Rule 1 |
| Endpoint and schema shapes (`GET /…`, table/column patterns) | Rule 1 |
| Credential vocabulary (`token`, `api key`, `credential`, `password`, `.env`) | Rule 1 |
| Hedge words adjacent to normative verbs (`must`, `required`, `shall`) | Rule 3 |

Keep the pattern list in `scripts/scrub-patterns.txt`, one pattern per line, comments with `#`.
Add a pattern whenever a review catches something the scan missed — **the scan's job is to stop
the same leak twice.**

## Sign-off

A skill is scrub-clean when a reviewer records, in the pull request:

```
Scrub checklist: PASS
  Rule 1 (internal ops):        clean / N removals
  Rule 2 (partner + roster):    clean / N removals
  Rule 3 (unattributed claims): clean / N cut — see ACCURACY-GATE.md sign-off
  Rule 4 (capability claims):   clean / N removals
  Mechanical scan:              N hits reviewed, N actioned
  Reviewer:                     <name>   Date: <YYYY-MM-DD>
```

"Clean" on a first pass over lifted material is a reason to look again, not a reason to merge.

## When a source fails the checklist

There are three valid outcomes, and only three:

1. **Scrub and ship** — the internal coupling was framing, and the material survives removal.
2. **Extract structure, discard prose** — the source is confidential but tells you what a skill
   on this topic must *cover*. Use it as a table of contents; write the content fresh against
   primary sources.
3. **Drop it** — the material is the confidential part. Record the decision and move on.

Outcome 3 is a successful run of this checklist, not a failure of it.
