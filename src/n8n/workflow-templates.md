---
title: 'Official n8n Workflow Templates | DevDeskApp'
description: 'The 7 published n8n templates built with n8n-nodes-devdeskapp: developer utilities, Indian CTC payroll, payment webhook audit, AI LLM JSON ingestion, offer letters, Meta CAPI and Notion to WordPress.'
---

# 🌟 Official Workflow Templates (n8n Community)

Seven templates built with `n8n-nodes-devdeskapp` are published on [n8n.io](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities/). Each one uses colour-coded sticky notes that explain the flow on the canvas, and you can import any of them by pasting the workflow JSON onto a canvas.

<div class="official-template-card" style="margin-bottom: 2rem;">
  <div class="template-card-left">
    <div class="template-card-header">
      <span class="template-badge">7 Live Templates</span>
      <span class="badge-live">Published on n8n.io</span>
    </div>
    <h3 class="template-card-title">Import in three steps</h3>
    <p class="template-card-desc">
      Install the node, copy a template from n8n.io, and press <code>Ctrl + V</code> on your n8n canvas.
    </p>
  </div>
  <a href="/templates/how-to-import" class="template-card-cta">
    <span>Import Guide</span>
    <span>→</span>
  </a>
</div>

---

## 📊 Template matrix

| ID | Template | DevDeskApp operations | Other integrations | Status |
| :--- | :--- | :--- | :--- | :--- |
| [#21017](/templates/developer-suite) | Developer Suite & Security Engine | prettify, hash, uuid, slugify, ctcToInHand | None | Runs as published |
| [#21130](/templates/ctc-salary-engine) | CTC to In-Hand Salary Engine | slugify, ctcToInHand, uuid, hash | None | Runs as published |
| [#21376](/templates/payment-webhook-sanitizer) | Payment Webhook Sanitizer | prettify, hash, uuid, slugify | Webhook, Slack | Runs as published |
| [#21593](/templates/ai-llm-postgres-ingest) | AI LLM JSON into Postgres | prettify, uuid, hash | Webhook, PostgreSQL, Slack | Fix after import |
| [#21594](/templates/offer-letter-generator) | CTC Offer Letter Generator | ctcToInHand, uuid, slugify, hash | Google Docs, Gmail, Google Sheets, Slack | Fix after import |
| [#21595](/templates/meta-capi-lead-sync) | Meta CAPI Lead Sync | caseConverter, hash, uuid, slugify | Webhook, Meta Graph API, Google Sheets, Slack | Fix after import |
| [#21596](/templates/notion-wordpress-publisher) | Notion to WordPress Publisher | slugify, hash, uuid, caseConverter | Notion, WordPress, Slack | Fix after import |

"Fix after import" means one or two parameters need changing before the workflow gives correct output. Each template page shows the exact fix.

---

## 1. Developer Suite & Security Engine (#21017)

A no-credentials demo of the main operations in one chain: format JSON, hash it with SHA-256, add a UUID, slugify a name and break down a CTC. The final Code node collects every result into one object.

<div class="doc-image">
  <img src="/images/fig-canvas-21017.png" alt="Template 21017 developer suite workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: Template #21017. <a href="/templates/developer-suite">Full page →</a></div>

---

## 2. CTC to In-Hand Salary Engine (#21130)

Creates an employee slug, UUID and payroll checksum, and turns an annual CTC into monthly gross, basic, employee and employer PF (capped at ₹1,800), professional tax, a new-regime TDS estimate and in-hand pay.

<div class="doc-image">
  <img src="/images/fig-canvas-21130.png" alt="Template 21130 CTC salary engine workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 2: Template #21130. <a href="/templates/ctc-salary-engine">Full page →</a></div>

---

## 3. Payment Webhook Sanitizer (#21376)

Receives a payment webhook, parses and formats the body, then adds a SHA-256 checksum, a UUID v4 trace ID and a slug, and alerts Slack. The checksum records what was received. It does not verify the provider's signature. Add the DevDeskApp **Webhook Signature Verifier** operation for that.

<div class="doc-image">
  <img src="/images/fig-canvas-21376.png" alt="Template 21376 payment webhook sanitizer workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 3: Template #21376. <a href="/templates/payment-webhook-sanitizer">Full page →</a></div>

---

## 4. Sanitize & Ingest AI LLM JSON into Postgres (#21593)

A Code node removes markdown fences from LLM output, DevDeskApp parses and formats the JSON, adds a trace UUID and a SHA-256 checksum, and an If node sends clean records to PostgreSQL and bad ones to Slack.

<div class="doc-image">
  <img src="/images/fig-canvas-21593.png" alt="Template 21593 AI LLM JSON ingestion workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 4: Template #21593. <a href="/templates/ai-llm-postgres-ingest">Full page and fix →</a></div>

---

## 5. Generate Indian CTC Offer Letters (#21594)

Calculates the salary breakdown, creates an offer UUID, candidate slug and compensation checksum, then fills a Google Docs letter, emails it with Gmail and alerts HR on Slack.

<div class="doc-image">
  <img src="/images/fig-canvas-21594.png" alt="Template 21594 CTC offer letter workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 5: Template #21594. <a href="/templates/offer-letter-generator">Full page and fix →</a></div>

---

## 6. Hash & Sync Leads to Meta CAPI (#21595)

Lowercases and SHA-256 hashes the lead email, adds an `event_id` UUID and a campaign slug, and sends opted-in leads to the Meta Conversions API with a Google Sheets log. Only the email is hashed and sent.

<div class="doc-image">
  <img src="/images/fig-canvas-21595.png" alt="Template 21595 Meta CAPI lead sync workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 6: Template #21595. <a href="/templates/meta-capi-lead-sync">Full page and fix →</a></div>

---

## 7. Publish Notion Blog Posts to WordPress (#21596)

Builds an SEO slug from the title, fingerprints the article HTML with SHA-256, adds a publication UUID and publishes approved posts through the WordPress node with a Slack alert.

<div class="doc-image">
  <img src="/images/fig-canvas-21596.png" alt="Template 21596 Notion to WordPress workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 7: Template #21596. <a href="/templates/notion-wordpress-publisher">Full page and fix →</a></div>

---

## ⏳ Submitted, waiting for review

- **#22360:** Auto-generate social media banners from RSS feeds with DevDeskApp, LinkedIn, X and Slack
- **#22361:** Convert GitHub PR schemas into Mermaid architecture diagrams with DevDeskApp, Slack and Notion
- **#22362:** Normalize CRM leads and validate JSON with DevDeskApp, PostgreSQL and Slack
- **#22363:** Detect payment fraud and deduplicate webhooks with DevDeskApp, PostgreSQL and Slack

---

## 💡 Import any template

1. Install `n8n-nodes-devdeskapp` ([installation guide](/n8n/installation)).
2. Open the template on n8n.io and click **Use for free**, or copy the workflow JSON.
3. Click an empty canvas and press `Ctrl + V` (Windows / Linux) or `Cmd + V` (macOS).

More detail and troubleshooting: [How to Import Templates](/templates/how-to-import).
