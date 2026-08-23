---
name: ddex-delivery
description: Problem-to-guidance router for DDEX delivery. Maps the thing that has gone wrong — a deal that dropped out, a territorial takedown, a malformed identifier, an artist credited wrongly, a parse failure, a flat-file report rejected — to the exact article in the DDEX knowledge base that answers it. Use when an ERN delivery fails or behaves unexpectedly, when deciding how to model deals, territories, identifiers or credits, when a DSP rejects a message, or when you need the authoritative DDEX guidance on a specific delivery problem.
---

# DDEX delivery — problem router

**What this is:** a map from *the problem you have* to *the DDEX guidance article that answers
it*. 209 articles across 11 problem areas, all from
[DDEX's own implementation guidance](https://kb.ddex.net/implementing-each-standard/electronic-release-notification-message-suite-%28ern%29/ern-implementation-guidance-and-best-practice).

**What it deliberately is not:** a summary of what those articles say. This skill routes; DDEX
asserts. Every line below is an article title and its link, grouped by symptom — the grouping is
ours, the content is DDEX's, and nothing here paraphrases a normative claim.

That design is deliberate. A previous skill in this catalog paraphrased ten DDEX standard
descriptions and a refutation pass found four of them materially wrong. Routing carries none of
that risk, and for a body of guidance this size the routing *is* the hard part — the articles are
excellent and very hard to find by search.

**Verified against primary sources: 2026-08-23.** Every link below was HTTP-checked on that date.

---

## Start here

| Question | Where it is answered |
|---|---|
| Which DDEX standard covers my problem at all? | The [`ddex-sources`](../ddex-sources/) skill in this catalog |
| Which release profile for which ERN version? | [Which Release Profile for which ERN Version?](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/which-release-profile-for-which-ern-version) |
| What is in a NewReleaseMessage? | [ERN 4 structure](https://kb.ddex.net/implementing-each-standard/electronic-release-notification-message-suite-%28ern%29/ern-4-explained/ern-4-structure) |
| What changed between ERN 3 and ERN 4? | [Differences between ERN 3 and ERN 4](https://kb.ddex.net/implementing-each-standard/electronic-release-notification-message-suite-%28ern%29/ern-4-explained/differences-between-ern-3-and-ern-4) |
| Which ERN 4 profiles exist? | [ERN 4 profiles](https://kb.ddex.net/implementing-each-standard/electronic-release-notification-message-suite-%28ern%29/ern-4-explained/ern-4-profiles) |
| How do I actually send it? | [ERN choreography using SFTP](https://kb.ddex.net/implementing-each-standard/electronic-release-notification-message-suite-%28ern%29/ern-choreography-using-secure-file-transfer-protocol) · [using web services](https://kb.ddex.net/implementing-each-standard/electronic-release-notification-message-suite-%28ern%29/ern-choreography-using-web-services) |
| Is there a worked example? | [ERN samples](https://kb.ddex.net/implementing-each-standard/electronic-release-notification-message-suite-%28ern%29/ern-samples) |

---

## Route by symptom

### Deals, dates and territories  ·  42 articles

Where most real delivery failures live. Availability windows, takedowns, territorial scope, and the dropout problem.

- [Active deals at time of sending an ERN](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/active-deals-at-time-of-sending-an-ern)
- [Adding tracks to a playlist before street date](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/adding-tracks-to-a-playlist-before-street-date)
- [Album streaming](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/album-streaming)
- [ApplicableTerritoryCode vs deal territories](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/applicableterritorycode-vs-deal-territories)
- [Availability and visibility](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/availability-and-visibility)
- [Avoiding "Dropouts" (or: how to signal Deal changes)](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/avoiding-dropouts-%28or%3A-how-to-signal-deal-changes%29)
- [Cancelling a Deal before Street Date](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/cancelling-a-deal-before-street-date)
- [Communicate territory information in different kinds of releases](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/communicate-territory-information-in-different-kinds-of-releases)
- [Communicating deal dates](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/communicating-deal-dates)
- [Communicating impact dates in MEAD and PIE](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/communicating-impact-dates-in-mead-and-pie)
- [Communicating old currencies](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/communicating-old-currencies)
- [Communicating right share percentages in MWN 1.3](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/communicating-right-share-percentages-in-mwn-1.3)
- [Complex deals can be dangerous](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/complex-deals-can-be-dangerous)
- [Dates in deals are being phased out in favour of datetimes](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/dates-in-deals-are-being-phased-out-in-favour-of-datetimes)
- [Deals without StartDate or StartDateTime](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/deals-without-startdate-or-startdatetime)
- [Displaying deal dates to consumers](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/displaying-deal-dates-to-consumers)
- [DoNotDisplayDates in ERN 4.3 and later](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/donotdisplaydates-in-ern-4.3-and-later)
- [Exclusive vs inclusive deals](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/exclusive-vs-inclusive-deals)
- [Handling conflicts in RDR](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/handling-conflicts-in-rdr)
- [LiveStream](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/livestream)
- [Multiple CommercialModelTypes or UseTypes in one deal](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/multiple-commercialmodeltypes-or-usetypes-in-one-deal)
- [Multiple consecutive deals](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/multiple-consecutive-deals)
- [Multiple deals for one release](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/multiple-deals-for-one-release)
- [NetAmount and NetRevenueInCurrencyOfAccounting](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/netamount-and-netrevenueincurrencyofaccounting)
- [NewReleaseMessage with no deal](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/newreleasemessage-with-no-deal)
- [No takedown in initial deal](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/no-takedown-in-initial-deal)
- [Podcasts in DSR](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/podcasts-in-dsr)
- [Recommended use of CommercialModelType and UseType in ERN-4](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/recommended-use-of-commercialmodeltype-and-usetype-in-ern-4)
- [Registering compilations in RDR-N 1.5](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/registering-compilations-in-rdr-n-1.5)
- [Reporting sales or usages for individual tracks](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/reporting-sales-or-usages-for-individual-tracks)
- [Revenue and IndirectValue](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/revenue-and-indirectvalue)
- [RightsClaimPolicy](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/rightsclaimpolicy)
- [Specifying a right share for an income participant](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/specifying-a-right-share-for-an-income-participant)
- [Start dates, end dates, start datetimes and end datetimes](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/start-dates%2C-end-dates%2C-start-datetimes-and-end-datetimes)
- [Takedowns](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/takedowns)
- [Tariff parameter types and values](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/tariff-parameter-types-and-values)
- [Territorial scope for visibility dates in ERN 4.3 and later](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/territorial-scope-for-visibility-dates-in-ern-4.3-and-later)
- [Territorial scope of a deal](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/territorial-scope-of-a-deal)
- [Territorial takedowns](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/territorial-takedowns)
- [Territories in deals and release descriptions](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/territories-in-deals-and-release-descriptions)
- [Updating a claim in RDR](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/updating-a-claim-in-rdr)
- [UseType for fingerprinting services](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/deals-and-commercial-aspects/usetype-for-fingerprinting-services)

### Release, resource and work metadata  ·  53 articles

The largest category: what goes in a release, what goes in a resource, and how the two relate.

- [Animated cover art](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/animated-cover-art)
- [Classical Music – Genre vs Structure](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/classical-music-%E2%80%93-genre-vs-structure)
- [Clip samples](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/clip-samples)
- [Communicating award information in MEAD and PIE](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-award-information-in-mead-and-pie)
- [Communicating classical releases and resources in ERN and RDR-N](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-classical-releases-and-resources-in-ern-and-rdr-n)
- [Communicating composite musical works in MWN 1.3](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-composite-musical-works-in-mwn-1.3)
- [Communicating focus tracks in MEAD and PIE](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-focus-tracks-in-mead-and-pie)
- [Communicating genres in ERN and which in MEAD](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-genres-in-ern-and-which-in-mead)
- [Communicating lyrics](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-lyrics)
- [Communicating mood in MEAD](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-mood-in-mead)
- [Communicating previews and clips used for shorts in ERN 4.3 and later](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-previews-and-clips-used-for-shorts-in-ern-4.3-and-later)
- [Communicating recording locations in MEAD and PIE](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-recording-locations-in-mead-and-pie)
- [Communicating stems](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-stems)
- [Communicating titles in ERN and MEAD](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/communicating-titles-in-ern-and-mead)
- [Contents of a RIN message](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/contents-of-a-rin-message)
- [Creation dates](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/creation-dates)
- [Differentiating versions using SubTitle in ERN and RDR-N](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/differentiating-versions-using-subtitle-in-ern-and-rdr-n)
- [Display Titles in RDR](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/display-titles-in-rdr)
- [ERN message without resources](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/ern-message-without-resources)
- [Genres](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/genres)
- [Handling immersive audio](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/handling-immersive-audio)
- [Handling of tracks that are not cleared](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/handling-of-tracks-that-are-not-cleared)
- [Hidden sound recordings](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/hidden-sound-recordings)
- [Images for box sets](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/images-for-box-sets)
- [Impact date](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/impact-date)
- [Keywords](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/keywords)
- [Linking different releases and resources](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/linking-different-releases-and-resources)
- [Metadata in different languages](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/metadata-in-different-languages)
- [Mixing classical with popular music](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/mixing-classical-with-popular-music)
- [Multiple instances of the same recording in the same release](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/multiple-instances-of-the-same-recording-in-the-same-release)
- [Original release date, release date and other dates](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/original-release-date%2C-release-date-and-other-dates)
- [Parental advice labels](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/parental-advice-labels)
- [PLine and CLine](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/pline-and-cline)
- [Pre-orders and instant gratification](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/pre-orders-and-instant-gratification)
- [Primary and secondary resources](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/primary-and-secondary-resources)
- [Product types in titles](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/product-types-in-titles)
- [Public domain works](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/public-domain-works)
- [RDR-N ResourceList](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/rdr-n-resourcelist)
- [ReferenceTitle of a SoundRecording](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/referencetitle-of-a-soundrecording)
- [Resource types](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/resource-types)
- [ResourceGroup hierarchies](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/resourcegroup-hierarchies)
- [ResourceGroups and TrackReleases](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/resourcegroups-and-trackreleases)
- [ResourceGroups are mandatory in ERN](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/resourcegroups-are-mandatory-in-ern)
- [Same recording with different metadata in different releases](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/same-recording-with-different-metadata-in-different-releases)
- [Samples for classical music in ERN-4](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/samples-for-classical-music-in-ern-4)
- [Sequencing resources](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/sequencing-resources)
- [Subtitles in multiple languages](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/subtitles-in-multiple-languages)
- [Territorial variations in release descriptions](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/territorial-variations-in-release-descriptions)
- [Territorial variations in the SoundRecordingDetailsByTerritory Composite in RDR-N](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/territorial-variations-in-the-soundrecordingdetailsbyterritory-composite-in-rdr-n)
- [Theme in MEAD](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/theme-in-mead)
- [Titles and subtitles in ERN-4](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/titles-and-subtitles-in-ern-4)
- [TrackReleases](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/trackreleases)
- [Translating and transliterating titles](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-releaseresourcework-metadata/translating-and-transliterating-titles)

### Artists, contributors and writers  ·  33 articles

Display artists versus contributors, roles, credits, name handling across scripts and spellings.

- [Artist name changes over time](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/artist-name-changes-over-time)
- [Artist roles and DisplayCredits](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/artist-roles-and-displaycredits)
- [Band members](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/band-members)
- [Canonical spellings for names](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/canonical-spellings-for-names)
- [Communicating awards in MEAD/PIE](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/communicating-awards-in-meadpie)
- [Communicating DisplayArtists and Contributors](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/communicating-displayartists-and-contributors)
- [Communicating DisplayArtists and DisplayArtistName](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/communicating-displayartists-and-displayartistname)
- [Communicating of focus tracks in MEAD/PIE](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/communicating-of-focus-tracks-in-meadpie)
- [Communicating remixes and remixers](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/communicating-remixes-and-remixers)
- [Contributors, artists and writers](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/contributors%2C-artists-and-writers)
- [Display artist overrides](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/display-artist-overrides)
- [DisplayArtistNames for releases and resources](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/displayartistnames-for-releases-and-resources)
- [DisplayArtistRoles](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/displayartistroles)
- [Displaying artists for remixes for ERN-4](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/displaying-artists-for-remixes-for-ern-4)
- [ERN-4 PartyList](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/ern-4-partylist)
- [Information on DisplayArtists, DisplayArtistNames, Contributors and IndirectContributors](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/information-on-displayartists%2C-displayartistnames%2C-contributors-and-indirectcontributors)
- [IsCredited and MayBeShared](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/iscredited-and-maybeshared)
- [Lengths of artist names](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/lengths-of-artist-names)
- [One artist with two roles](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/one-artist-with-two-roles)
- [Ownership claims for Single-Resource Releases in ERN](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/ownership-claims-for-single-resource-releases-in-ern)
- [Rights controller information in ERNs to Music Licensing Companies](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/rights-controller-information-in-erns-to-music-licensing-companies)
- [Role code synonyms and credits](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/role-code-synonyms-and-credits)
- [Roles and instrumentation in performances](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/roles-and-instrumentation-in-performances)
- [Semantics of LineupComplete](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/semantics-of-lineupcomplete)
- [Sequencing recording artists and writers](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/sequencing-recording-artists-and-writers)
- [Special characters](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/special-characters)
- [Splitting names and the importance of the KeyName](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/splitting-names-and-the-importance-of-the-keyname)
- [Statements for Contributor and RightsController revenues](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/statements-for-contributor-and-rightscontroller-revenues)
- [Territorial rights controller information](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/territorial-rights-controller-information)
- [Translating and Transliterating Names](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/translating-and-transliterating-names)
- [Various artists in ERN](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/various-artists-in-ern)
- [Why artist information is in multiple places](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/why-artist-information-is-in-multiple-places)
- [Writer roles](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-contributors%2C-artists-and-writers/writer-roles)

### Identifiers, codes and dates  ·  20 articles

ISRCs, barcodes, DPIDs, proprietary identifiers, territory codes, and the date-versus-datetime distinction.

- [Avoiding the use of proprietary Identifiers](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/avoiding-the-use-of-proprietary-identifiers)
- [Bar codes of various lengths](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/bar-codes-of-various-lengths)
- [Can a release be identified by an ISRC?](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/can-a-release-be-identified-by-an-isrc)
- [Communicating territories in MWN 1.3](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/communicating-territories-in-mwn-1.3)
- [Communication of identifiers in DDEX messages](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/communication-of-identifiers-in-ddex-messages)
- [Do DPIDs have hyphens?](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/do-dpids-have-hyphens)
- [How many DPIDs Do I need?](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/how-many-dpids-do-i-need)
- [Identifiers for resources and releases and parties](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/identifiers-for-resources-and-releases-and-parties)
- [Identifying chapters](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/identifying-chapters)
- [Identifying sound recordings and videos containing the same audio](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/identifying-sound-recordings-and-videos-containing-the-same-audio)
- [Limitations of proprietary identifiers](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/limitations-of-proprietary-identifiers)
- [Malformed identifiers](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/malformed-identifiers)
- [Multiple proprietary identification systems](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/multiple-proprietary-identification-systems)
- [Opus and composer catalogue numbers](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/opus-and-composer-catalogue-numbers)
- [ProductionDate vs. CreationDate](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/productiondate-vs.-creationdate)
- [Proprietary identifiers](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/proprietary-identifiers)
- [Territory codes using ISO 3166-1 or ISO 3166-3 or TIS](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/territory-codes-using-iso-3166-1-or-iso-3166-3-or-tis)
- [The importance of ISRCs](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/the-importance-of-isrcs)
- [Use of ISRCs as the primary database key](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/use-of-isrcs-as-the-primary-database-key)
- [Worldwide](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-identifiers%2C-iso-codes-lists-and-dates/worldwide)

### Messages, batches and choreography  ·  13 articles

How messages move: credentials, acknowledgements, batching, ordering, inserts versus updates.

- [Access credentials](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/access-credentials)
- [Acknowledgements and non-repudiation](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/acknowledgements-and-non-repudiation)
- [Differentiating inserts from updates](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/differentiating-inserts-from-updates)
- [ERN messages as a statements of truth](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/ern-messages-as-a-statements-of-truth)
- [File naming convention for DSR masterlist reports](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/file-naming-convention-for-dsr-masterlist-reports)
- [Generating and processing ERN batches](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/generating-and-processing-ern-batches)
- [MEAD information for a taken-down release](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/mead-information-for-a-taken-down-release)
- [MEAD messages as a statement of truth](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/mead-messages-as-a-statement-of-truth)
- [MEAD messages as secondary resources in an ERN feed](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/mead-messages-as-secondary-resources-in-an-ern-feed)
- [No resources in initial delivery](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/no-resources-in-initial-delivery)
- [Order of ERN processing](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/order-of-ern-processing)
- [Prioritisation of ERN messages](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/prioritisation-of-ern-messages)
- [Signalling rights conflicts in ERN-C status updates](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-message-exchange-protocols-and-choreographies/signalling-rights-conflicts-in-ern-c-status-updates)

### XML issues  ·  13 articles

Encoding, namespaces, XSD locations, special characters, and the traps that break a parse.

- [Comments](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/comments)
- [Direction of writing](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/direction-of-writing)
- [Do not use CDATA to concatenate data](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/do-not-use-cdata-to-concatenate-data)
- [Handling 'odd' characters](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/handling-%27odd%27-characters)
- [Importing RIN files into RIN files (RIN 1.0 only)](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/importing-rin-files-into-rin-files-%28rin-1.0-only%29)
- [Java library's date bug for 2020](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/java-library%27s-date-bug-for-2020)
- [Locations of XSDs](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/locations-of-xsds)
- [Namespace and file locations for the XSD for allowed value sets](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/namespace-and-file-locations-for-the-xsd-for-allowed-value-sets)
- [Order of XML attributes](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/order-of-xml-attributes)
- [Preambles for XML-based DDEX messages](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/preambles-for-xml-based-ddex-messages)
- [Referencing composites using ID and IDREF](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/referencing-composites-using-id-and-idref)
- [Semantics of repeating XML tags](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/semantics-of-repeating-xml-tags)
- [Special XML characters (and how to avoid &amp;amp;)](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-xml-issues/special-xml-characters-%28and-how-to-avoid-%26amp%3Bamp%3B%29)

### General guidance on messages  ·  17 articles

Cross-cutting: versions, field lengths, invalid messages, uncommon use cases.

- [Cardinality of the RightShareType element in MWN 1.1](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/cardinality-of-the-rightsharetype-element-in-mwn-1.1)
- [Communication of percentages](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/communication-of-percentages)
- [Currency conversion in DSR and CDM](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/currency-conversion-in-dsr-and-cdm)
- [Date/time tags and Time Zone Designators](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/datetime-tags-and-time-zone-designators)
- [Dealing with uncommon use cases](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/dealing-with-uncommon-use-cases)
- [Field length and precision](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/field-length-and-precision)
- [GDPR and UGC](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/gdpr-and-ugc)
- [Invalid Messages](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/invalid-messages)
- [Origin and trustworthiness of MEAD and PIE information](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/origin-and-trustworthiness-of-mead-and-pie-information)
- [Precision of numeric values in MWN](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/precision-of-numeric-values-in-mwn)
- [Priorities for metadata items](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/priorities-for-metadata-items)
- [Scalability of UGC sales/usage reports](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/scalability-of-ugc-salesusage-reports)
- [Time stamp for data accuracy](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/time-stamp-for-data-accuracy)
- [Version compatibility](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/version-compatibility)
- [What can I do if I have data requirements not addressed by DDEX](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/what-can-i-do-if-i-have-data-requirements-not-addressed-by-ddex)
- [Which Release Profile for which ERN Version?](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/which-release-profile-for-which-ern-version)
- [Who owns which rights?](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/general-guidance-on-messages/who-owns-which-rights)

### Flat-file issues (DSR, CDM, RDR-R)  ·  8 articles

The reporting side: delimiters, long titles, spreadsheet exports, mandatory fields with no data.

- [Delimiters and special characters in flat file messages](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-for-flat-file-issues/delimiters-and-special-characters-in-flat-file-messages)
- [Deprecated Cells in DSR, CDM and RDR-R](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-for-flat-file-issues/deprecated-cells-in-dsr%2C-cdm-and-rdr-r)
- [DSR and CDM messages exported from spreadsheet applications](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-for-flat-file-issues/dsr-and-cdm-messages-exported-from-spreadsheet-applications)
- [Handling long titles and special characters in the DSR, CDM and RDR-R standards](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-for-flat-file-issues/handling-long-titles-and-special-characters-in-the-dsr%2C-cdm-and-rdr-r-standards)
- [MRBV vs SRBV](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-for-flat-file-issues/mrbv-vs-srbv)
- [Multiple identifiers for multiple parties in flat-file standards](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-for-flat-file-issues/multiple-identifiers-for-multiple-parties-in-flat-file-standards)
- [No data for mandatory fields](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-for-flat-file-issues/no-data-for-mandatory-fields)
- [Profile names in DSR and CDM](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-for-flat-file-issues/profile-names-in-dsr-and-cdm)

### Allowed value sets and code lists  ·  6 articles

AVS versioning, user-defined values, specialising DDEX-defined values.

- [Common language and script code combinations](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-allowed-value-sets-%28avs%2C-aka-code-lists%29/common-language-and-script-code-combinations)
- [Excluded Territories and Worldwide](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-allowed-value-sets-%28avs%2C-aka-code-lists%29/excluded-territories-and-worldwide)
- [Specialising DDEX-Defined Values](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-allowed-value-sets-%28avs%2C-aka-code-lists%29/specialising-ddex-defined-values)
- [Specifying CWR instrumentations in MWN 1.3](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-allowed-value-sets-%28avs%2C-aka-code-lists%29/specifying-cwr-instrumentations-in-mwn-1.3)
- [User-defined values](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-allowed-value-sets-%28avs%2C-aka-code-lists%29/user-defined-values)
- [Versioning Allowed Value Sets](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-allowed-value-sets-%28avs%2C-aka-code-lists%29/versioning-allowed-value-sets)

### Previews  ·  2 articles

- [Preview resources](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-previews/preview-resources)
- [Resource-specific previews](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-previews/resource-specific-previews)

### Binaries  ·  2 articles

- [Adding and removing specific encodings](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-binaries/adding-and-removing-specific-encodings)
- [Communicating binaries](https://kb.ddex.net/implementing-each-standard/best-practices-for-all-ddex-standards/guidance-on-binaries/communicating-binaries)
---

## Coverage and limits

**209 articles across 11 areas**, taken from DDEX's ERN implementation-guidance index on
2026-08-23. The index also carries guidance specific to other standards — DSR, MWN, RDR, CDM,
RIN, MWL, LOD, BWARM and the MLC choreographies. Those are **not** routed here: this skill is
scoped to delivery. Use [`ddex-sources`](../ddex-sources/) to find the right standard first.

**The grouping is ours; the categories follow DDEX's own hierarchy.** Where an article appears
under more than one DDEX category it is listed once, in the area where the problem usually
presents.

**This skill will go stale.** DDEX adds and reorganises guidance. The counts and links above are
a snapshot dated at the top of this file. If a link is dead or an area has grown,
[tell us](https://github.com/Royalti-io/royalti-skills/issues) — for a router, a dead link is the
only real defect there is.

**No claim is made about what any article says.** If a title reads as though it answers your
question and the article does not, that is a mis-grouping on our part, not a contradiction of
DDEX. Report it the same way.

## Sources

Every link routes into [DDEX's knowledge base](https://kb.ddex.net). Provenance, including the
link-check run, is in [`references/sources.json`](references/sources.json).
