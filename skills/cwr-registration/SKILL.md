---
name: cwr-registration
description: How publishers register musical works with performing rights organisations using Common Works Registration (CWR) — the MusicMark route to ASCAP, BMI and SOCAN, the mandatory test phase, file naming, SFTP endpoints, acknowledgment types and status codes, and how work IDs are assigned by territory. Use when onboarding to CWR submission, when a registration file is rejected or held, when interpreting a 1st or 2nd acknowledgment, when deciding between CWR and EBR, or when you need to know where the CWR specification comes from and why you cannot download it.
---

# CWR registration — the North American route

**What this covers:** the *process* of registering works by CWR — how you onboard, how files are
named and transmitted, what comes back, and what the responses mean.

**What it does not cover, deliberately:** the CWR file format itself — record types, field
layouts, validation rules. That material lives in a specification that is not publicly
available, and this catalog does not publish claims it cannot cite. See
[Getting the specification](#getting-the-specification).

**Verified against primary sources: 2026-08-21.**

---

## What CWR is

Common Works Registration is a CISAC electronic data-exchange format that gives publishers and
societies a standard way to register works. Its current operational version is **2.2**.

CISAC lists CWR alongside its other exchange formats — CRD, AVI/AVTT/AVR, UDS/UPA, CAF, WID — on
its [formats page](https://www.cisac.org/formats).

**What CWR does not support.** DDEX published a gap analysis against CWR v3.0 recording that CWR
does not presently provide support for: the musical work licensing process; Letters of Direction;
communicating a UGC policy for a work (track/monetize/block); sending audio files relating to a
work, such as for fingerprinting; communicating lyrics; communicating print-rights information;
or communicating UseTypes — the sub-categories of mechanical, performing and synch rights.

That list is worth reading before assuming CWR is the right vehicle for a problem. Several of
those gaps are why DDEX's MWN standard exists — MWN was designed for the complexities of works
licensing in territories without central licensing infrastructure, such as the US and Canada, and
its version 1.3 added features for registering works with CMOs.

## Getting the specification

**You cannot download it.** CISAC's public formats page describes CWR and links a **member-only**
document pack. Publishers seeking the current functional specification are directed to contact
their CWR representative at ASCAP, BMI or SOCAN.

One substantive CWR document is public: the
[Common Works Registration User Manual](https://musicmark.com/documents/cwr11-1494_cwr_user_manual_2011-09-23_e_2011-09-23_en.pdf)
hosted by MusicMark — document reference `CWR11-1494`, 54 pages, dated 23 September 2011.

**Treat it as historical.** It documents **v2.1**; the current operational version is 2.2. It is
useful for orientation and for understanding the shape of the format, and it should not be relied
on for current field-level behaviour. Where this skill draws on it, that is flagged inline.

## Two batch routes: CWR and EBR

MusicMark accepts batch registrations in either format:

- **CWR** — the industry-standard text format for music registration.
- **EBR** — Electronic Batch Registration, a simplified spreadsheet (Excel) format for batch
  registrations.

EBR is the lower-effort path if you are not already producing CWR. This skill covers the CWR
route; the choice between them is a question of what your systems already emit.

## MusicMark: one file, three societies

MusicMark is a collaboration between **ASCAP, BMI and SOCAN** to make works registration more
efficient and create a unified copyright picture in North America. For publishers the practical
effect is that you submit and receive files through **one SFTP site rather than three**, and
receive **one common first acknowledgment** rather than one from each PRO.

Society codes appear in file names and acknowledgments:

| Code | Organisation |
|---|---|
| `010` | ASCAP |
| `021` | BMI |
| `101` | SOCAN |
| `707` | MusicMark |

## The test phase is mandatory

Every publisher wishing to register CWR files with MusicMark must complete a test phase. The
sequence:

1. Publisher contacts MusicMark.
2. A representative issues SFTP credentials; the publisher uploads a test CWR file to the **test**
   SFTP site — **no more than 100 works per file**.
3. MusicMark runs the file in the test environment and generates a **1st Acknowledgment within
   24–48 hours** of submission. The publisher is emailed when it is ready for pickup.
4. The publisher retrieves the 1st Acknowledgment and processes it in their own system.
5. Each PRO generates a **2nd Acknowledgment**, per the agreed testing schedule.
6. If a second test file is needed, MusicMark says so.
7. After a successful test phase, MusicMark promotes the publisher to production.

**What to put in a test file.** MusicMark asks for a spread representative of your catalogue,
exercising a broad range of business cases — ASCAP, BMI and SOCAN works with foreign parties;
works with foreign writers collecting more than 100% of the writing share; chain of title (links);
co-publishing agreements; administration agreements; sub-publishing agreements.

That list is effectively a test plan. A file of clean, single-publisher, single-territory works
will pass testing and teach you nothing about how your real catalogue behaves.

## File naming

The CWR process is automated and recognises only an explicit naming standard. **Files that do not
follow the convention are rejected.**

```
CWyynnnnsss_707.Vxx
```

| Element | Meaning |
|---|---|
| `CW` | Prefix identifying CWR |
| `yy` | Year |
| `nnnn` | Sequence number assigned by the publisher |
| `sss` | Sender code — 2 or 3 characters for a publisher, or the 3-digit society code |
| `707` | Recipient — 707 is MusicMark |
| `Vxx` | CWR version in use |

**Note for existing submitters:** publishers currently indicate either `000` or the receiving
society code in the file name. Publishers already approved as CWR submitters either continue
using `000` or change the file name to `707`.

## Transmission

SFTP, port 22.

| Environment | Endpoint |
|---|---|
| Test | `sftp://qaftp.musicmark.com` |
| Production | `sftp://ftp.musicmark.com` |

Test and production credentials are **different**; production credentials are emailed on
approval. MusicMark names FileZilla and WinSCP as third-party clients. Connection problems are
directed to your own network administrator and firewall settings, which in practice means
outbound SFTP has to be open before you start.

## Acknowledgments

### 1st Acknowledgment

Returned after MusicMark validates the file. It differs from a single-society acknowledgment in
three ways:

- the header record indicates `707MUSICMARK` rather than a specific society name and code
- the file name indicates `707`
- **work ID numbers are not included**

Status types in the MusicMark 1st ACK: `RA` transaction accepted · `RJ` transaction rejected ·
`DU` duplicate registration · `NP` no territory of US or Canada.

**The operational detail that matters most:** if a file is rejected, **all subsequent files are
placed on hold** until the rejected file is corrected and reposted to the SFTP site *under the
same file name*. Once the corrected file is accepted, held files process automatically in the
order received.

That is a queue-blocking failure. A rejected file left uncorrected stops everything behind it, and
the fix requires reusing the original file name rather than submitting a new one.

### 2nd Acknowledgments

Each participating society then returns its own acknowledgment via MusicMark, with the society
code in the file name. Delivery is generally within 24–48 hours of the 1st ACK; SOCAN's
subsequent acknowledgments are generated daily and its quarterly acknowledgment reports all
accepted transactions that became payment-ready in the quarter.

Status types vary by society and by acknowledgment round. Across them you will see:

| Code | Meaning |
|---|---|
| `RA` | Transaction accepted |
| `AS` | Registration accepted — as sent |
| `AC` | Registration accepted — with changes |
| `RJ` | Transaction rejected |
| `DU` | Duplicate registration |
| `NP` | No participation / not licensed by that society |
| `CO` | Conflict (BMI) |
| `RC` | Publisher claim to the work rejected (BMI) |

ASCAP and BMI generate subsequent 2nd ACKs whenever a work record is updated — so acknowledgments
continue to arrive after the initial registration cycle, and a pipeline that only expects them
during onboarding will drop them.

## Work IDs and No Participation

**Work IDs are assigned by territory**, which is the part that surprises people:

- ASCAP and BMI load works and assign work IDs when the transaction record includes the territory
  of the **US**.
- SOCAN loads and assigns work IDs when the transaction record includes the territory of
  **Canada**.
- All three assign IDs when the transaction includes both US and Canada.

**`NP` means different things in different rounds.** In the MusicMark 1st acknowledgment, an `NP`
indicates the title is not intended to be registered for US and/or Canadian territories. In a
PRO's 2nd acknowledgment, an `NP` **still generates a work ID** but indicates the title is not
intended for licensing by that specific PRO.

## Going live

Once MusicMark determines testing is complete, the publisher is notified of approval to submit in
production and issued separate production SFTP credentials. The upload, notification and
acknowledgment-retrieval process is otherwise unchanged from testing.

## Scope limits

This skill is **North America via MusicMark**. It does not cover:

- **The CWR format itself** — see [Getting the specification](#getting-the-specification).
- **Publisher and writer share mechanics.** No public primary source was found for this, and the
  catalog does not publish uncited claims. If you know of one,
  [tell us](https://github.com/Royalti-io/royalti-skills/issues).
- **Routes outside North America** — PRS, SESAC, ICE and other societies. Not researched; their
  absence here is not a statement that CWR is unavailable through them.
- **Mechanical rights registration.** CWR is used for registration with mechanical rights
  societies as well as PROs, but the mechanical route is not covered here. For the US mechanical
  licensing data standard specifically, see DDEX's MWDR.

## Sources

Read these rather than trusting this page. Every claim above is traced to one of them, with the
section located, in [`references/sources.json`](references/sources.json).

| Source | Authoritative for | Note |
|---|---|---|
| [MusicMark — CWR Registration: Getting Started](https://musicmark.com/documents/MusicMark-getting-started.pdf) | The entire onboarding process: test phase, file naming, SFTP, acknowledgments, work IDs, going live | The primary source for almost everything on this page |
| [MusicMark — Frequently Asked Questions](https://musicmark.com/documents/MusicMark-FAQs.pdf) | CWR vs EBR; what MusicMark is | |
| [CISAC — Electronic Data Exchange Formats](https://www.cisac.org/formats) | CWR's status as a CISAC format; specification access | |
| [DDEX — MWN and the Common Works Registration](https://kb.ddex.net/implementing-each-standard/musical-work-data-and-rights-communication-%28mwdr%29/musical-work-right-share-notification-standard-%28mwn%29/mwn-explained/mwn-and-the-common-works-registration-%28cwr%29/) | Current CWR version; what CWR does not support | |
| [CWR User Manual `CWR11-1494`](https://musicmark.com/documents/cwr11-1494_cwr_user_manual_2011-09-23_e_2011-09-23_en.pdf) | The format's shape, historically | **2011 · v2.1 · low confidence.** Cited for its existence and vintage only — no field-level claim on this page rests on it |

**Documentation moves.** If something here is wrong,
[open an issue](https://github.com/Royalti-io/royalti-skills/issues) — a sourced correction is the
most useful thing you can send.
