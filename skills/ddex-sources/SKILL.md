---
name: ddex-sources
description: Curated index of primary sources for music delivery — the DDEX standards (ERN, MEAD, PIE, DSR, MWDR, RDR, CDM, LRAW, RIN, AR) and the official metadata and onboarding documentation for major DSPs, aggregators and regional platforms. Use when you need the authoritative source for a delivery, metadata or reporting requirement, when checking which DDEX standard covers a problem, when a claim about a DSP's requirements needs a citation, or when onboarding to a new platform and looking for its provider documentation.
---

# Music delivery — primary source index

**What this is:** a link-checked index of the documents that are actually authoritative for
music delivery, metadata and reporting. Nothing here is a summary of those documents. When a
question about a requirement matters, the answer is in the source, and this tells you which
source and where.

**Why it exists as a skill:** the hard part of this domain is rarely reasoning — it is knowing
that the answer lives in DDEX's CDM standard rather than ERN, or that a DSP's metadata rules sit
in a style guide separate from its onboarding guide. That routing knowledge is what this encodes.

**Verified against primary sources: 2026-08-21.**
**Reviewed and signed off: 2026-08-22** — Chinedum Okerengwor, Royalti.io. Scrub
checklist and accuracy gate both PASS; see
[`references/sources.json`](references/sources.json) for the per-claim record. Every URL below was checked on that date, and
every description of a DDEX standard was checked against that standard's own overview text. See
[Verification](#verification).

---

## DDEX standards

[DDEX](https://ddex.net) publishes the message standards the delivery chain runs on. The
[knowledge base](https://kb.ddex.net) is the implementation documentation, and
[the standards index](https://kb.ddex.net/implementing-each-standard/) lists all of them.

Which standard covers what — descriptions taken from each standard's own overview:

| Standard | Covers | Reach for it when |
|---|---|---|
| [ERN](https://kb.ddex.net/implementing-each-standard/electronic-release-notification-message-suite-%28ern%29) — Electronic Release Notification | Releases and resources, and the terms and conditions under which a DSP may make them available to consumers | Delivering a release; a DSP rejects a message; deal terms or territories are wrong |
| [MEAD](https://kb.ddex.net/implementing-each-standard/media-enrichment-and-description-%28mead%29) — Media Enrichment and Description | Rich supplementary metadata about parties, releases, resources and musical works — supplements the core supply-chain and rights data carried by ERN | A release needs descriptive metadata beyond what ERN carries |
| [PIE](https://kb.ddex.net/implementing-each-standard/party-identification-and-enrichment-%28pie%29) — Party Identification and Enrichment | Rich information about Parties. Same role as MEAD, but PIE focuses on parties where MEAD focuses on content | Party and artist profile data; disambiguating a party |
| [DSR](https://kb.ddex.net/implementing-each-standard/digital-sales-reporting-message-suite-%28dsr%29) — Digital Sales Reporting | Sales and usage reports created by licensees (the digital services) and sent to licensors (the rights owners of works, recordings and videos). Flat-file; it replaced an XML-formatted report | Ingesting statements; reconciling reported usage |
| [MWDR](https://kb.ddex.net/implementing-each-standard/musical-work-data-and-rights-communication-%28mwdr%29) — Musical Work Data and Rights Communication | Obtaining licences for the **mechanical right** in musical works, **for companies based in the US**. Formerly the Works Notification and Licensing Standards | US mechanical licensing between a record company or DSP and the works rights holders |
| [RDR](https://kb.ddex.net/implementing-each-standard/recording-data-and-rights-standards-%28rdr%29) — Recording Data and Rights Standards | Data exchanged between music licensing companies, record companies and performer representatives — sound recordings, music videos, and the sales and usage data underpinning royalty calculation across territories | Record company and performer rights, and the data behind royalty distribution, across multiple territories |
| [CDM](https://kb.ddex.net/implementing-each-standard/claim-detail-message-suite-%28cdm%29) — Claim Detail Message Suite | Claims in **musical works** and the **invoice calculations** relating to them, exchanged between works rights owners or licensors and DSPs — plus a way for DSPs to flag discrepancies | Reconciling claims and invoices on musical works with a DSP |
| [LRAW](https://kb.ddex.net/implementing-each-standard/links-between-resources-and-musical-works-%28lraw%29) — Links Between Resources and Musical Works | **Communicating** a link you have already established between a sound or video recording and the musical work(s) it embodies — including the negative case, that a work is *not* embodied | Telling business partners which work a recording embodies, or that it does not |
| [RIN](https://kb.ddex.net/implementing-each-standard/recording-information-notification-%28rin%29) — Recording Information Notification | Metadata captured at the point of recording — designed to be integrated into studio equipment and software including DAWs, then communicated onward with the audio | Credits and session metadata originating in the studio |
| [AR](https://kb.ddex.net/implementing-each-standard/anomaly-reporting-%28ar%29) — Anomaly Reporting | **Anomalous consumer engagement** with a release, resource, work or artist — which may or may not be fraudulent — and a message for a partner to respond. Delivery anomalies are *not* covered yet | Suspected streaming fraud or unusual consumption patterns |

Two cross-cutting guides worth reading before implementing any of the above:

- [Best practices for all DDEX standards](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards) — includes the deals and commercial-aspects
  material that causes most real-world delivery failures
- [Best practices for catalogue transfers](https://kb.ddex.net/implementing-each-standard/best-practices-for-catalogue-transfers) — moving a catalogue between distributors

**A note on scope.** ERN gets most of the attention and covers least of the problem. If your
question is about reported money it is probably DSR; if it is about claims and invoicing on
works, CDM; if it is about which work a recording embodies, LRAW. **MWDR is narrower than its
name suggests** — it is the mechanical right, for US-based companies, and it is not a general
publishing-data standard. Checking which standard owns the question first saves more time than
any other habit in this domain.

---

## Digital service providers

### Tier 1

| Platform | Document |
|---|---|
| Spotify | [Style guide](https://artists.spotify.com/help/article/style-guide) · [Metadata style guide](https://support.spotify.com/us/artists/article/metadata-style-guide/) |
| Apple Music | [Music specification](https://help.apple.com/itc/musicspec/en.lproj/static.html) · [Style guide](https://help.apple.com/itc/musicstyleguide/en.lproj/static.html) · [Provider support](https://itunespartner.apple.com/music/) |
| YouTube Music | [Artist hub](https://artists.youtube.com) |
| Amazon Music | [Amazon Music for Artists](https://artists.amazonmusic.com) |

### Tier 2

| Platform | Document |
|---|---|
| Tidal | [Artist portal](https://artists.tidal.com) |
| Deezer | [Developer portal](https://developers.deezer.com) |
| Pandora | [Artist Marketing Platform](https://amp.pandora.com) |
| SoundCloud | [SoundCloud for Artists](https://artists.soundcloud.com) |

### Regional

| Platform | Region | Document |
|---|---|---|
| Tencent Music (QQ Music) | China | [Open platform](https://open.y.qq.com) |
| NetEase Cloud Music | China | [Platform](https://music.163.com) |
| JioSaavn | India | [Site](https://www.jiosaavn.com) |
| Anghami | Middle East / North Africa | [Artist portal](https://artists.anghami.com) |

---

## Aggregators and distributors

| Company | Document |
|---|---|
| FUGA | [Knowledge base](https://support.fuga.com/hc/en-us) · [Webhooks guide](https://support.fuga.com/hc/en-us/articles/28485420930324-FUGA-Webhooks-User-Guide) · [Spotify content policy guidelines](https://support.fuga.com/hc/en-us/articles/30023468817300-Spotify-Content-Policy-Guidelines) |
| The Orchard | [Site](https://theorchard.com) |

---

## Verification

### Links

Checked 2026-08-21. Status is reported as observed, not as assumed:

| Status | Meaning | Entries |
|---|---|---|
| `verified` | Returned HTTP 200 to an automated check | 29 |
| `blocked-to-automated-checks` | Returned 403 or 406 to an automated request. **Bot protection, not evidence the page is gone** — but not confirmed in a browser either, so not claimed to work | Tidal, Anghami, FUGA (×3) |
| `unverified` | Could not be checked from our environment | Believe — omitted from the tables above rather than listed as working |

**Six links in the source material this index was built from were wrong and have been repaired.**
Amazon's developer portal, SoundCloud's artist page, and DDEX's MEAD and PIE paths all returned
404; two Spotify PDF links had truncated paths and were replaced with live style-guide pages.

### Claims

Every description in the DDEX table was checked against that standard's own overview text, by a
pass whose instruction was to **refute** it. Of ten:

- **3 confirmed** as drafted — ERN, DSR, RIN
- **3 corrected** — MEAD and PIE carried examples the source does not support; RDR used a term
  the source does not use and omitted half its scope
- **4 refuted and rewritten** — MWDR, CDM, LRAW and AR were materially wrong, not merely loose

The refutations are recorded per claim in
[`references/sources.json`](references/sources.json), with what the draft said and why it failed.
They are kept rather than quietly fixed: **a skill that shows where it was wrong is easier to
trust than one that only shows its conclusions.**

**Documentation moves, and so do standards.** If something here is wrong,
[tell us](https://github.com/Royalti-io/royalti-skills/issues) — that is the most useful
correction this skill can receive.

---

## What this skill will not tell you

It will not tell you what a field means, what a DSP requires, or whether your message will
validate. It tells you **where the answer is authoritative**. Read the source; the source is the
content.

It is also not a substitute for a DDEX membership or a provider agreement. Some material — full
XSDs, provider-specific onboarding packs — is available only to members and partners, and this
index links the public entry points, not the material behind them.
