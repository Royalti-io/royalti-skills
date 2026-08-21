
# Accuracy gate

Every normative claim in this repo carries a citation to a primary source and has survived an
attempt to refute it. This is a **merge blocker**, not a guideline.

## What counts as a normative claim

A statement about how a specification, format, standard, registry or submission route **works**
— what a field means, what is required, what a system will accept or reject, what a record type
contains, where a submission goes.

Normative:

> The ERN `ReleaseProfileVersionId` determines which validation profile applies.

Not normative:

> If you are new to ERN, start with the release profile before the deal terms — the profile
> constrains what the rest of the message can say.

The second is structural guidance and needs no citation. It also must not be dressed up as a
requirement: **"you must start with the release profile" would be a normative claim**, and a
false one. Watch the verb.

## Primary sources

In descending order of authority:

| Rank | Source | Notes |
|---|---|---|
| 1 | The standards body's own specification or knowledge base | DDEX knowledge base; the CISAC CWR specification |
| 2 | The operating organisation's own published documentation | A PRO's submission documentation; a registry's published schema |
| 3 | Official developer or partner documentation from the system in question | Versioned and dated where possible |

**Not primary**, and not sufficient on their own:

- Another skill, blog post, wiki, or LLM output — including this repo
- A vendor's marketing page describing what it supports
- Forum posts, unless from the standards body or operator in an official capacity
- Institutional memory. **"I know this because I have done it" is not a citation.** It is a lead
  to a source, and the source is what gets cited.

Where only a secondary source exists, either the claim is cut, or it is restated as clearly
attributed observation — "in practice, X commonly does Y" — never as specification.

## Cite-or-cut

**An uncitable normative claim is deleted, not softened.**

This is the rule that does the real work, because the failure mode it prevents is not lying —
it is hedging. A claim you cannot source does not become safe by acquiring a "generally" or a
"typically". It becomes unfalsifiable, which is worse: the reader still takes it as guidance and
you have removed your own ability to check it later.

Applying the rule:

1. Draft the claim.
2. Find the primary source. Record it in `references/sources.json`.
3. If there is no primary source — **delete the sentence.** Do not reword it. Do not move it to
   a "notes" section. Do not add a hedge.
4. If deleting it leaves a gap the skill genuinely needs, that gap is a finding: report it, and
   decide whether the skill's scope was right.

**Expect the skills to come out smaller than drafted.** A thin, fully-cited skill is the
intended outcome. A comprehensive-looking one built on institutional memory is the failure this
gate exists to prevent.

## Recording provenance

Every skill carries `references/sources.json`, following the model this repo inherited from its
source material: typed sources, per-source confidence against a stated rubric, access dates,
key excerpts with a relevance note, and back-references to where each source is used.

One addition on top of that model, and it is the load-bearing one:

```json
"claims": [
  {
    "id": "c1",
    "section": "ERN message structure",
    "claim": "<the normative sentence, as it appears in SKILL.md>",
    "sourceId": 1,
    "locator": "<section / page / anchor within the source>",
    "verifiedOn": "YYYY-MM-DD",
    "verdict": "confirmed"
  }
]
```

**Claim-level, not document-level.** A `sources.json` that lists three authoritative URLs at the
bottom of a skill proves nothing about any individual sentence. The back-reference has to run
from the claim to the exact place in the source that supports it, or the citation is decoration.

Each skill also carries a dated verification stamp:

```
Verified against primary sources: YYYY-MM-DD
```

Specifications move. A stamp that is old is honest; a stamp that is absent is not.

## Adversarial verification

Because the reviewer of this material is also, in practice, its author, an independent
confirmation pass would confirm. So the pass is adversarial by construction.

**Procedure**, run before sign-off on every skill:

1. Extract every normative claim in the skill as a flat list.
2. For each claim, an independent verifier — with no access to the drafting rationale — is
   given the claim and the cited source and asked to **refute** it: does the source actually
   say this? Does it say it for this version, this profile, this territory? Does it say
   something narrower that the claim has generalised?
3. The verifier defaults to **refuted** when uncertain. Ambiguity is a refutation, not a pass.
4. Where a claim can fail in more than one way, verify it through more than one lens — does the
   source support it, does it still hold for the current version, and would a practitioner
   recognise it as true in practice.
5. The verifier returns, per claim: `confirmed` · `refuted` · `unverifiable`.

**The reviewer reads the exceptions, not the document.** `refuted` and `unverifiable` claims go
back through cite-or-cut. `confirmed` claims are merged.

Two rules that keep this honest:

- **A verifier that confirms everything has failed.** A clean first pass over lifted material is
  a reason to re-run with a sharper prompt, not a reason to merge.
- **No silent caps.** If the pass sampled rather than covered, or dropped claims it could not
  parse, that is stated in the sign-off. A partial run reported as complete is worse than no run.

## Sign-off

Recorded in the pull request, alongside the scrub checklist sign-off:

```
Accuracy gate: PASS
  Normative claims extracted:   N
  Cited to primary source:      N
  Cut under cite-or-cut:        N
  Adversarial pass:             N confirmed · N refuted · N unverifiable
  Refuted/unverifiable handled: cut / re-sourced / rescoped
  Coverage:                     full  (or: state exactly what was not covered)
  Verified-against stamp:       YYYY-MM-DD
  Reviewer:                     <name>   Date: <YYYY-MM-DD>
```

## What this gate does not do

It does not make the material correct. It makes the material **checkable** — every claim traceable
to something a reader can open and disagree with. That is a lower bar than truth and a far higher
one than confidence, and for published specification material it is the bar that matters.
