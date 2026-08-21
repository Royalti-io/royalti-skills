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
that the answer lives in DDEX's MWDR standard rather than ERN, or that a DSP's metadata rules
sit in a style guide separate from its onboarding guide. That routing knowledge is what this
encodes.

**Verified against primary sources: 2026-08-21.** Every URL below was checked on that date.
Status is recorded honestly per entry — see [Link status](#link-status).

---

## DDEX standards

[DDEX](https://ddex.net) publishes the message standards the delivery chain runs on. The
[knowledge base](https://kb.ddex.net) is the implementation documentation, and
[the standards index](https://kb.ddex.net/implementing-each-standard/) lists all of them.

Which standard covers what:

| Standard | Covers | Reach for it when |
|---|---|---|
| [ERN](https://kb.ddex.net/implementing-each-standard/electronic-release-notification-message-suite-%28ern%29) — Electronic Release Notification | Releases, resources, deals — the delivery message itself | Delivering a release; a DSP rejects a message; deal terms or territories are wrong |
| [MEAD](https://kb.ddex.net/implementing-each-standard/media-enrichment-and-description-%28mead%29) — Media Enrichment and Description | Editorial and marketing metadata beyond the release | Enriching a release with moods, themes, focus tracks |
| [PIE](https://kb.ddex.net/implementing-each-standard/party-identification-and-enrichment-%28pie%29) — Party Identification and Enrichment | Artist and party identity, images, biography | Artist profiles, party identifiers, disambiguating a name |
| [DSR](https://kb.ddex.net/implementing-each-standard/digital-sales-reporting-message-suite-%28dsr%29) — Digital Sales Reporting | Sales and usage reporting from DSP back to rights holder | Ingesting statements; reconciling reported usage |
| [MWDR](https://kb.ddex.net/implementing-each-standard/musical-work-data-and-rights-communication-%28mwdr%29) — Musical Work Data and Rights Communication | Musical works, writers, publishers, shares | Publishing-side work data; the composition, not the recording |
| [RDR](https://kb.ddex.net/implementing-each-standard/recording-data-and-rights-standards-%28rdr%29) — Recording Data and Rights Standards | Recording-side rights and ownership data | Neighbouring rights; who controls a recording where |
| [CDM](https://kb.ddex.net/implementing-each-standard/claim-detail-message-suite-%28cdm%29) — Claim Detail Message Suite | Claims against usage | Reconciling disputed or conflicting claims |
| [LRAW](https://kb.ddex.net/implementing-each-standard/links-between-resources-and-musical-works-%28lraw%29) — Links Between Resources and Musical Works | The recording↔work link | Matching an ISRC to its underlying composition |
| [RIN](https://kb.ddex.net/implementing-each-standard/recording-information-notification-%28rin%29) — Recording Information Notification | Studio and session data captured at creation | Credits and session metadata from the recording session |
| [AR](https://kb.ddex.net/implementing-each-standard/anomaly-reporting-%28ar%29) — Anomaly Reporting | Reporting problems back upstream | A partner needs structured notice that data is wrong |

Two cross-cutting guides worth reading before implementing any of the above:

- [Best practices for all DDEX standards](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards) — includes the deals and commercial-aspects
  material that causes most real-world delivery failures
- [Best practices for catalogue transfers](https://kb.ddex.net/implementing-each-standard/best-practices-for-catalogue-transfers) — moving a catalogue between distributors

**A note on scope.** ERN gets most of the attention and covers least of the problem. If your
question is about money it is probably DSR; if it is about a composition it is probably MWDR or
LRAW. Checking which standard owns the question first saves more time than any other habit in
this domain.

---

## Digital service providers

### Tier 1

| Platform | Document | What it is authoritative for |
|---|---|---|
| Spotify | [Style guide](https://artists.spotify.com/help/article/style-guide) · [Metadata style guide](https://support.spotify.com/us/artists/article/metadata-style-guide/) | Title, artist and version formatting; what gets rejected |
| Apple Music | [Music specification](https://help.apple.com/itc/musicspec/en.lproj/static.html) · [Style guide](https://help.apple.com/itc/musicstyleguide/en.lproj/static.html) · [Provider support](https://itunespartner.apple.com/music/) | The most detailed public DSP spec; asset and metadata requirements |
| YouTube Music | [Artist hub](https://artists.youtube.com) | Channel and topic behaviour, Content ID interaction |
| Amazon Music | [Amazon Music for Artists](https://artists.amazonmusic.com) | Artist-side profile and catalogue behaviour |

### Tier 2

| Platform | Document |
|---|---|
| Tidal | [Artist portal](https://artists.tidal.com) |
| Deezer | [Developer portal](https://developers.deezer.com) |
| Pandora | [Artist Marketing Platform](https://amp.pandora.com) |
| SoundCloud | [SoundCloud for Artists](https://artists.soundcloud.com) |

### Regional

Frequently missing from English-language write-ups, and where onboarding surprises concentrate.

| Platform | Region | Document |
|---|---|---|
| Tencent Music (QQ Music) | China | [Open platform](https://open.y.qq.com) |
| NetEase Cloud Music | China | [Platform](https://music.163.com) |
| JioSaavn | India | [Site](https://www.jiosaavn.com) |
| Anghami | Middle East / North Africa | [Artist portal](https://artists.anghami.com) |

---

## Aggregators and distributors

Their public documentation is often the clearest account of what downstream DSPs require,
because they have to explain it to their own clients.

| Company | Document |
|---|---|
| FUGA | [Knowledge base](https://support.fuga.com/hc/en-us) · [Webhooks guide](https://support.fuga.com/hc/en-us/articles/28485420930324-FUGA-Webhooks-User-Guide) · [Spotify content policy guidelines](https://support.fuga.com/hc/en-us/articles/30023468817300-Spotify-Content-Policy-Guidelines) |
| The Orchard | [Site](https://theorchard.com) |

---

## Link status

Checked 2026-08-21. Status is reported as observed, not as assumed:

| Status | Meaning | Entries |
|---|---|---|
| `verified` | Returned HTTP 200 to an automated check | 29 |
| `blocked-to-automated-checks` | Returned 403 or 406 to an automated request. **This is bot protection, not evidence the page is gone** — but we did not confirm it in a browser, so we do not claim it works | Tidal, Anghami, FUGA (×3) |
| `unverified` | Could not be checked from our environment | Believe — omitted from the tables above rather than listed as working |

Per-entry detail, including what each source is cited for, is in
[`references/sources.json`](references/sources.json).

**Six links in the source material this index was built from were wrong and have been repaired.**
Amazon's developer portal, SoundCloud's artist page, and DDEX's MEAD and PIE paths all returned
404; two Spotify PDF links had truncated paths and were replaced with the live style-guide pages.
**Documentation moves.** If a link here is dead,
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
