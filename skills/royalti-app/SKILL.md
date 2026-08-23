---
name: royalti-app
description: Task router for the Royalti.io web app — maps what you are trying to do (import a royalty statement, set up splits, create a product or asset, merge artists, register works via CWR, deliver to stores, read analytics, manage payments) to the Royalti help article that covers it. Use when working in the Royalti workspace and looking for how a feature works, or when helping someone use Royalti. For the REST API, use the royalti-api skill instead.
---

# Royalti.io — task router

**What this is:** a map from *what you are trying to do* to *the Royalti help article that
covers it*. 46 articles, regrouped by task rather than by the help centre's own categories.

**What it is not:** a substitute for the help centre, and not a description of how features
behave. This routes; the help centre documents. Nothing here restates what an article says, so
nothing here can go stale against the product while the links stay good.

**The app is at [app.royalti.io](https://app.royalti.io).** For the REST API, use the
[`royalti-api`](https://github.com/Royalti-io/royalti-api-skill) skill; for the underlying
industry standards, [`ddex-delivery`](../ddex-delivery/), [`ddex-sources`](../ddex-sources/) and
[`cwr-registration`](../cwr-registration/) in this catalog.

**Verified against primary sources: 2026-08-23.** All 46 links checked; all resolve.

---

## Orientation

Three words do most of the work in Royalti, and the help centre's
[Glossary](https://royalti.io/help/glossary-of-terms) is the authority on the rest:

| Term | What it is |
|---|---|
| **Asset** | An individual track — a sound recording or video |
| **Product** | Also called a release; made up of at least one asset |
| **Split** | How royalties divide between collaborators on a track |

Other entry points on the site: [Features](https://royalti.io/features) ·
[Pricing](https://royalti.io/pricing) · [Developers](https://royalti.io/developers) ·
[DDEX](https://royalti.io/ddex) · [Publishing](https://royalti.io/publishing) ·
[Changelog](https://royalti.io/changelog) · [Help centre](https://royalti.io/help)

---

## Route by task

### Getting started

New workspace, first upload, what the words mean.

- [Welcome to Royalti.io](https://royalti.io/help/welcome-to-royaltiio)
- [Frequently Asked Questions](https://royalti.io/help/frequently-asked-questions)
- [Glossary of Terms](https://royalti.io/help/glossary-of-terms)
- [How to Use Magic-Link Authentication on Account](https://royalti.io/help/how-to-use-magic-link-authentication-on-account)

### Catalog — products, assets, artists

Assets are tracks; products (releases) are made of them.

- [Catalog](https://royalti.io/help/catalog)
- [Product Management](https://royalti.io/help/product-management)
- [Create a Product on Royalti.io](https://royalti.io/help/create-a-product-on-royaltiio)
- [Assets Management](https://royalti.io/help/assets-management)
- [Creating an Asset on Royalti.io](https://royalti.io/help/creating-an-asset-on-royaltiio)
- [Artist Management](https://royalti.io/help/artist-management)
- [Create an Artist on Royalti.io](https://royalti.io/help/create-an-artist-on-royaltiio)
- [Use the Merge Artist Functionality on Royalti.io](https://royalti.io/help/use-the-merge-artist-functionality-on-royaltiio)
- [Bulk Import Assets from CSV](https://royalti.io/help/bulk-import-assets-from-csv)
- [Bulk Import Products from CSV](https://royalti.io/help/bulk-import-products-from-csv)
- [Using the Checklist Page](https://royalti.io/help/using-the-checklist-page)
- [How to Download Metadata for Products on Royalti.io](https://royalti.io/help/how-to-download-metadata-for-products-on-royaltiio)

### Royalty data — importing and sending

Getting statements in, and getting data back out.

- [How to Import Royalty Data](https://royalti.io/help/how-to-import-royalty-data)
- [Managing Royalty Sources](https://royalti.io/help/managing-royalty-sources)
- [Royalty Processing and Exchange Rates](https://royalti.io/help/royalty-processing-and-exchange-rates)
- [Download and Send Royalty Data](https://royalti.io/help/download-and-send-royalty-data)

### Splits

How the money divides.

- [Split Management](https://royalti.io/help/split-management)
- [Time Based Splits Guide](https://royalti.io/help/time-based-splits-guide)

### Accounting and payments

- [Accounting Management in Royalti.io](https://royalti.io/help/accounting-management-in-royaltiio)
- [Adding Financial Transactions in Royalti.io: New Payment, New Expense, New Revenue](https://royalti.io/help/adding-financial-transactions-in-royaltiio-new-payment-new-expense-new-revenue)
- [Managing Revenue in Royalti.io](https://royalti.io/help/managing-revenue-in-royaltiio)
- [Managing Payment Items in Royalti.io](https://royalti.io/help/managing-payment-items-in-royaltiio)
- [Payment Method Management](https://royalti.io/help/payment-method-management)
- [Managing Wallets and Beneficiaries with Verto on Royalti.io](https://royalti.io/help/managing-wallets-and-beneficiaries-with-verto-on-royaltiio)

### Publishing and CWR

- [Publishing and CWR Guide](https://royalti.io/help/publishing-and-cwr-guide)

### Distribution and delivery

- [Using the Distro Addon in Royalti.io](https://royalti.io/help/using-the-distro-addon-in-royaltiio)
- [Activating and Managing the Releases Feature - The Admin](https://royalti.io/help/activating-and-managing-the-releases-feature-the-admin)
- [Activating and Managing the Releases Feature - The User Guide](https://royalti.io/help/activating-and-managing-the-releases-feature-the-user-guide)
- [Import Catalog from DSPs](https://royalti.io/help/import-catalog-from-dsps)

### Analytics and reporting

- [Understanding Royalti Analytics Reports](https://royalti.io/help/understanding-royalti-analytics--reports)

### Users, workspace and settings

- [User Management](https://royalti.io/help/user-management)
- [Create a User (Person) on Royalti.io](https://royalti.io/help/create-a-user-person-on-royaltiio)
- [Updating My Workspace Settings on Royalti.io](https://royalti.io/help/updating-my-workspace-settings-on-royaltiio)
- [Royalti.io Notification System](https://royalti.io/help/royaltiio-notification-system)

### Ask Roy and the MCP server

Royalti's built-in AI assistant, and connecting your own.

- [Ask Roy your AI Assistant](https://royalti.io/help/ask-roy-your-ai-assistant)
- [How to Use Ask Roy - Royalti AI Assistant Guide](https://royalti.io/help/how-to-use-ask-roy-royaltis-ai-assistant)
- [Ask Roy Capabilities - Queries, Actions & Workflows](https://royalti.io/help/ask-roy-capabilities)
- [25 Example Questions for Ask Roy](https://royalti.io/help/ask-roy-example-questions)
- [Setting Up the Royalti MCP Server](https://royalti.io/help/setting-up-the-royalti-mcp-server)

### Not grouped

Articles in the help centre that did not fit a task above.

- [Delivering to Stores with DDEX FUGA](https://royalti.io/help/delivering-to-stores-with-ddex--fuga)
- [Untitled article](https://royalti.io/help/untitled-article)
- [🚀 Getting Started with Royalti.io](https://royalti.io/help/getting-started-with-royaltiio)
---

## Coverage and limits

**46 articles, every one link-checked on 2026-08-23.** That is the entire public help centre at
that date, across its eight categories — two of which (`roster-management` and `addon`) render
with no articles.

**The grouping is ours.** The help centre's own categories put accounting, authentication and
workspace settings under "Catalog Management"; this router regroups by task. Where an article
could sit in two places it appears once, under the task it most answers.

**Titles are as published.** Eight are derived from the article URL because those pages do not
set a server-side title; one article is published under the title "Untitled article". Neither is
corrected here — a router that renames things stops matching what you see on the site.

**No claim is made about how any feature behaves.** If an article title reads as though it
answers your question and the article does not, that is a mis-grouping on our part. If the
article is out of date, that is for the help centre.
[Tell us either way](https://github.com/Royalti-io/royalti-skills/issues).

## Sources

The [Royalti help centre](https://royalti.io/help) and the royalti.io site. Per-article
provenance and the link-check run are in
[`references/sources.json`](references/sources.json).
