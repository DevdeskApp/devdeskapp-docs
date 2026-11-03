---
title: 'Official n8n Workflow Templates'
description: 'Catalog of 7 official DevDeskApp n8n templates: AI LLM ingestion, CTC payroll, payment webhook sanitizer, Meta CAPI sync, and Notion CMS publishing.'
---

# 📋 Official n8n Workflow Templates

Discover and deploy production-ready n8n automation blueprints built with **`n8n-nodes-devdeskapp`**. The DevDeskApp nodes in every template run inside your n8n process and make no external API calls, so the data they format, hash or calculate stays on your instance.

<div class="official-template-card">
  <div class="template-card-left">
    <div class="template-card-header">
      <span class="template-badge">7 Verified Blueprints</span>
      <span class="badge-live">Official n8n Creator Portal</span>
    </div>
    <h3 class="template-card-title">1-Click n8n Canvas Import</h3>
    <p class="template-card-desc">
      All templates can be imported directly into your local or cloud n8n editor. Copy the template JSON or open the direct n8n.io link and press <code>Ctrl+V</code> (or <code>Cmd+V</code>) inside your workflow canvas.
    </p>
  </div>
  <a href="/templates/how-to-import" class="template-card-cta">
    <span>Import Guide</span>
    <span>→</span>
  </a>
</div>

---

## 🌟 Templates Catalog (7 Published Live)

Each template has its own page with the node order, parameters and a real execution result. Templates marked **Fix after import** need one small change, listed on their page.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin: 2rem 0;">

  <!-- Template 1: Developer Suite -->
  <div style="border: 1px solid var(--vp-c-border); border-radius: 16px; padding: 1.5rem; background: var(--vp-c-bg-soft); display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s ease, border-color 0.2s ease;" class="pipeline-step">
    <div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
        <span style="font-size: 0.75rem; font-weight: 700; color: #6366f1; background: rgba(99, 102, 241, 0.12); border: 1px solid rgba(99, 102, 241, 0.3); padding: 2px 8px; border-radius: 9999px;">
          TEMPLATE #21017
        </span>
        <span class="badge-live" style="font-size: 0.7rem;">Live on n8n.io</span>
      </div>
      <h3 style="margin: 0 0 0.5rem 0; font-size: 1.15rem; font-weight: 700; color: var(--vp-c-text-1);">
        Developer Suite & Security Engine
      </h3>
      <p style="font-size: 0.88rem; color: var(--vp-c-text-2); line-height: 1.5; margin: 0 0 1rem 0;">
        Sequential 5-operation pipeline: JSON prettification, SHA-256 cryptographic hashing, RFC 4122 v4 UUID tracing, SEO slug generation, and CTC salary breakdown.
      </p>
      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 1.25rem;">
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">JSON Prettifier</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">SHA-256 Digest</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">UUID v4</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Slugifier</span>
      </div>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap; padding-top: 1rem; border-top: 1px solid var(--vp-c-border);">
      <a href="/templates/developer-suite" style="flex: 1; text-align: center; padding: 8px 12px; border-radius: 8px; background: #6366f1; color: white !important; font-size: 0.82rem; font-weight: 700; text-decoration: none;">
        View Blueprint →
      </a>
      <a href="https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities/" target="_blank" rel="noopener" style="padding: 8px 12px; border-radius: 8px; border: 1px solid var(--vp-c-border); background: var(--vp-c-bg); color: var(--vp-c-text-1) !important; font-size: 0.82rem; font-weight: 600; text-decoration: none;">
        n8n Portal ↗
      </a>
    </div>
  </div>

  <!-- Template 2: CTC Salary Engine -->
  <div style="border: 1px solid var(--vp-c-border); border-radius: 16px; padding: 1.5rem; background: var(--vp-c-bg-soft); display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s ease, border-color 0.2s ease;" class="pipeline-step">
    <div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
        <span style="font-size: 0.75rem; font-weight: 700; color: #10b981; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3); padding: 2px 8px; border-radius: 9999px;">
          TEMPLATE #21130
        </span>
        <span class="badge-live" style="font-size: 0.7rem;">Live on n8n.io</span>
      </div>
      <h3 style="margin: 0 0 0.5rem 0; font-size: 1.15rem; font-weight: 700; color: var(--vp-c-text-1);">
        Employee CTC to In-Hand Salary Engine
      </h3>
      <p style="font-size: 0.88rem; color: var(--vp-c-text-2); line-height: 1.5; margin: 0 0 1rem 0;">
        Turns an annual CTC into monthly gross, basic, employee and employer PF (capped at ₹1,800), professional tax, a new-regime TDS estimate and in-hand pay.
      </p>
      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 1.25rem;">
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Payroll Automation</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Statutory PF</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">In-Hand Calculation</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">HR Tech</span>
      </div>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap; padding-top: 1rem; border-top: 1px solid var(--vp-c-border);">
      <a href="/templates/ctc-salary-engine" style="flex: 1; text-align: center; padding: 8px 12px; border-radius: 8px; background: #10b981; color: white !important; font-size: 0.82rem; font-weight: 700; text-decoration: none;">
        View Blueprint →
      </a>
      <a href="https://n8n.io/workflows/21130-generate-indian-ctc-offers-and-payroll-breakdowns-with-devdeskapp/" target="_blank" rel="noopener" style="padding: 8px 12px; border-radius: 8px; border: 1px solid var(--vp-c-border); background: var(--vp-c-bg); color: var(--vp-c-text-1) !important; font-size: 0.82rem; font-weight: 600; text-decoration: none;">
        n8n Portal ↗
      </a>
    </div>
  </div>

  <!-- Template 3: Payment Webhook Sanitizer -->
  <div style="border: 1px solid var(--vp-c-border); border-radius: 16px; padding: 1.5rem; background: var(--vp-c-bg-soft); display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s ease, border-color 0.2s ease;" class="pipeline-step">
    <div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
        <span style="font-size: 0.75rem; font-weight: 700; color: #f59e0b; background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.3); padding: 2px 8px; border-radius: 9999px;">
          TEMPLATE #21376
        </span>
        <span class="badge-live" style="font-size: 0.7rem;">Live on n8n.io</span>
      </div>
      <h3 style="margin: 0 0 0.5rem 0; font-size: 1.15rem; font-weight: 700; color: var(--vp-c-text-1);">
        Payment Webhook Sanitizer & Security Audit
      </h3>
      <p style="font-size: 0.88rem; color: var(--vp-c-text-2); line-height: 1.5; margin: 0 0 1rem 0;">
        Audit pipeline for payment webhooks: parses and formats the JSON body, records a SHA-256 checksum, a UUID v4 trace ID and a slug, and alerts Slack through an If gate.
      </p>
      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 1.25rem;">
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Webhook Sanitizer</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">SHA-256 Digest</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">UUID v4 Audit</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Payment Security</span>
      </div>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap; padding-top: 1rem; border-top: 1px solid var(--vp-c-border);">
      <a href="/templates/payment-webhook-sanitizer" style="flex: 1; text-align: center; padding: 8px 12px; border-radius: 8px; background: #f59e0b; color: white !important; font-size: 0.82rem; font-weight: 700; text-decoration: none;">
        View Blueprint →
      </a>
      <a href="https://n8n.io/workflows/21376-sanitize-and-audit-payment-webhooks-with-devdeskapp-json-and-crypto-tools/" target="_blank" rel="noopener" style="padding: 8px 12px; border-radius: 8px; border: 1px solid var(--vp-c-border); background: var(--vp-c-bg); color: var(--vp-c-text-1) !important; font-size: 0.82rem; font-weight: 600; text-decoration: none;">
        n8n Portal ↗
      </a>
    </div>
  </div>

  <!-- Template 4: AI LLM JSON Ingestion -->
  <div style="border: 1px solid var(--vp-c-border); border-radius: 16px; padding: 1.5rem; background: var(--vp-c-bg-soft); display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s ease, border-color 0.2s ease;" class="pipeline-step">
    <div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
        <span style="font-size: 0.75rem; font-weight: 700; color: #6366f1; background: rgba(99, 102, 241, 0.12); border: 1px solid rgba(99, 102, 241, 0.3); padding: 2px 8px; border-radius: 9999px;">
          TEMPLATE #21593
        </span>
        <span class="badge-live badge-amber" style="font-size: 0.7rem;">Fix after import</span>
      </div>
      <h3 style="margin: 0 0 0.5rem 0; font-size: 1.15rem; font-weight: 700; color: var(--vp-c-text-1);">
        Sanitize & Ingest AI LLM JSON into Postgres
      </h3>
      <p style="font-size: 0.88rem; color: var(--vp-c-text-2); line-height: 1.5; margin: 0 0 1rem 0;">
        A Code node strips markdown fences from LLM output, then DevDeskApp formats the JSON, adds a UUID v4 trace ID and a SHA-256 checksum before the PostgreSQL insert and Slack log.
      </p>
      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 1.25rem;">
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">AI Agent Ingest</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Markdown fences</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">PostgreSQL</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Slack Alerts</span>
      </div>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap; padding-top: 1rem; border-top: 1px solid var(--vp-c-border);">
      <a href="/templates/ai-llm-postgres-ingest" style="flex: 1; text-align: center; padding: 8px 12px; border-radius: 8px; background: #6366f1; color: white !important; font-size: 0.82rem; font-weight: 700; text-decoration: none;">
        View Blueprint →
      </a>
      <a href="https://n8n.io/workflows/21593-sanitize-and-ingest-ai-llm-json-into-postgres-with-devdeskapp-and-slack/" target="_blank" rel="noopener" style="padding: 8px 12px; border-radius: 8px; border: 1px solid var(--vp-c-border); background: var(--vp-c-bg); color: var(--vp-c-text-1) !important; font-size: 0.82rem; font-weight: 600; text-decoration: none;">
        n8n Portal ↗
      </a>
    </div>
  </div>

  <!-- Template 5: Indian CTC Offer Letter Generator -->
  <div style="border: 1px solid var(--vp-c-border); border-radius: 16px; padding: 1.5rem; background: var(--vp-c-bg-soft); display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s ease, border-color 0.2s ease;" class="pipeline-step">
    <div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
        <span style="font-size: 0.75rem; font-weight: 700; color: #10b981; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3); padding: 2px 8px; border-radius: 9999px;">
          TEMPLATE #21594
        </span>
        <span class="badge-live badge-amber" style="font-size: 0.7rem;">Fix after import</span>
      </div>
      <h3 style="margin: 0 0 0.5rem 0; font-size: 1.15rem; font-weight: 700; color: var(--vp-c-text-1);">
        Generate Indian CTC Offer Letters with Docs & Gmail
      </h3>
      <p style="font-size: 0.88rem; color: var(--vp-c-text-2); line-height: 1.5; margin: 0 0 1rem 0;">
        CTC to in-hand breakdown (basic, PF, PT, TDS), an offer UUID, a candidate slug and a compensation checksum, then a Google Docs letter, Gmail delivery and a Slack HR alert.
      </p>
      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 1.25rem;">
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">HR Automation</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Google Docs</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Gmail</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">PF / PT Breakdown</span>
      </div>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap; padding-top: 1rem; border-top: 1px solid var(--vp-c-border);">
      <a href="/templates/offer-letter-generator" style="flex: 1; text-align: center; padding: 8px 12px; border-radius: 8px; background: #10b981; color: white !important; font-size: 0.82rem; font-weight: 700; text-decoration: none;">
        View Blueprint →
      </a>
      <a href="https://n8n.io/workflows/21594-generate-indian-ctc-offer-letters-with-devdeskapp-google-docs-gmail-and-slack/" target="_blank" rel="noopener" style="padding: 8px 12px; border-radius: 8px; border: 1px solid var(--vp-c-border); background: var(--vp-c-bg); color: var(--vp-c-text-1) !important; font-size: 0.82rem; font-weight: 600; text-decoration: none;">
        n8n Portal ↗
      </a>
    </div>
  </div>

  <!-- Template 6: Meta CAPI Lead Sync -->
  <div style="border: 1px solid var(--vp-c-border); border-radius: 16px; padding: 1.5rem; background: var(--vp-c-bg-soft); display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s ease, border-color 0.2s ease;" class="pipeline-step">
    <div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
        <span style="font-size: 0.75rem; font-weight: 700; color: #a855f7; background: rgba(168, 85, 247, 0.12); border: 1px solid rgba(168, 85, 247, 0.3); padding: 2px 8px; border-radius: 9999px;">
          TEMPLATE #21595
        </span>
        <span class="badge-live badge-amber" style="font-size: 0.7rem;">Fix after import</span>
      </div>
      <h3 style="margin: 0 0 0.5rem 0; font-size: 1.15rem; font-weight: 700; color: var(--vp-c-text-1);">
        Hash & Sync Leads to Meta CAPI with Google Sheets
      </h3>
      <p style="font-size: 0.88rem; color: var(--vp-c-text-2); line-height: 1.5; margin: 0 0 1rem 0;">
        Lowercases and SHA-256 hashes the lead email for Meta CAPI, adds a UUID v4 event_id and campaign slug, and posts opted-in leads to the Graph API with a Google Sheets log.
      </p>
      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 1.25rem;">
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Meta CAPI</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">SHA-256 Privacy</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Google Sheets</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Conversion Sync</span>
      </div>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap; padding-top: 1rem; border-top: 1px solid var(--vp-c-border);">
      <a href="/templates/meta-capi-lead-sync" style="flex: 1; text-align: center; padding: 8px 12px; border-radius: 8px; background: #a855f7; color: white !important; font-size: 0.82rem; font-weight: 700; text-decoration: none;">
        View Blueprint →
      </a>
      <a href="https://n8n.io/workflows/21595-hash-and-sync-leads-to-meta-capi-with-devdeskapp-google-sheets-and-slack/" target="_blank" rel="noopener" style="padding: 8px 12px; border-radius: 8px; border: 1px solid var(--vp-c-border); background: var(--vp-c-bg); color: var(--vp-c-text-1) !important; font-size: 0.82rem; font-weight: 600; text-decoration: none;">
        n8n Portal ↗
      </a>
    </div>
  </div>

  <!-- Template 7: Notion to WordPress SEO Publisher -->
  <div style="border: 1px solid var(--vp-c-border); border-radius: 16px; padding: 1.5rem; background: var(--vp-c-bg-soft); display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s ease, border-color 0.2s ease;" class="pipeline-step">
    <div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
        <span style="font-size: 0.75rem; font-weight: 700; color: #ec4899; background: rgba(236, 72, 153, 0.12); border: 1px solid rgba(236, 72, 153, 0.3); padding: 2px 8px; border-radius: 9999px;">
          TEMPLATE #21596
        </span>
        <span class="badge-live badge-amber" style="font-size: 0.7rem;">Fix after import</span>
      </div>
      <h3 style="margin: 0 0 0.5rem 0; font-size: 1.15rem; font-weight: 700; color: var(--vp-c-text-1);">
        Publish SEO-Safe Notion Blog Posts to WordPress
      </h3>
      <p style="font-size: 0.88rem; color: var(--vp-c-text-2); line-height: 1.5; margin: 0 0 1rem 0;">
        Builds an SEO slug from the article title, fingerprints the HTML with SHA-256, adds a UUID v4 publication ID and publishes approved posts through the WordPress node with a Slack alert.
      </p>
      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 1.25rem;">
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Notion CMS</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">WordPress API</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">SEO Slugifier</span>
        <span style="font-size: 0.72rem; padding: 2px 6px; border-radius: 6px; background: var(--vp-c-bg-mute); color: var(--vp-c-text-2);">Slack Alerts</span>
      </div>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap; padding-top: 1rem; border-top: 1px solid var(--vp-c-border);">
      <a href="/templates/notion-wordpress-publisher" style="flex: 1; text-align: center; padding: 8px 12px; border-radius: 8px; background: #ec4899; color: white !important; font-size: 0.82rem; font-weight: 700; text-decoration: none;">
        View Blueprint →
      </a>
      <a href="https://n8n.io/workflows/21596-publish-seo-safe-notion-blog-posts-to-wordpress-with-devdeskapp-and-slack/" target="_blank" rel="noopener" style="padding: 8px 12px; border-radius: 8px; border: 1px solid var(--vp-c-border); background: var(--vp-c-bg); color: var(--vp-c-text-1) !important; font-size: 0.82rem; font-weight: 600; text-decoration: none;">
        n8n Portal ↗
      </a>
    </div>
  </div>

</div>

---

## ⏳ Upcoming Templates (Under n8n Community Review)

These 4 workflows are submitted to the n8n Creator Portal and waiting for review:

| Template ID | Workflow Name | Key Operations | Target Pipeline |
| :--- | :--- | :--- | :--- |
| **#22360** | RSS-based Social Banner Publisher | Slugifier, SHA-256, UUID v4 | LinkedIn, X & Slack automated multi-platform broadcasting |
| **#22361** | GitHub PR Architecture Diagram Sync | Slugifier, SHA-256 | GitHub Pull Requests, Slack alerts & Notion Architecture Hub |
| **#22362** | CRM Lead Normalizer & Deduplication | Prettifier, SHA-256, UUID v4 | HubSpot, Salesforce, PostgreSQL & Slack pipeline |
| **#22363** | Real-Time Fraud & Webhook Deduplication | SHA-256, UUID v4, Condition Gate | Stripe/Razorpay anti-replay defense & Slack incident escalation |

---

## ⚡ Quick 1-Click Import Instructions

Importing any DevDeskApp workflow into your n8n workspace requires only 3 simple steps:

1. **Install Node:** Ensure `n8n-nodes-devdeskapp` is installed in your n8n instance ([Installation Guide](/n8n/installation)).
2. **Copy the template:** Open it on n8n.io and click **Use for free**, or copy the workflow JSON.
3. **Paste in Canvas:** Open your n8n canvas and press **`Ctrl + V`** (or **`Cmd + V`**). All nodes, parameters and connections appear on the canvas.

Detailed step-by-step instructions with troubleshooting can be found in our [Import Guide](/templates/how-to-import).

---

## 🚀 Future Templates & Submissions

Have you built a creative automation pipeline using `n8n-nodes-devdeskapp`?
- **AI Agent Automation**: Connecting DevDeskApp tools to autonomous agents.
- **Data Engineering**: High-throughput JSON sanitization before PostgreSQL or Snowflake ingestion.
- **Enterprise DevOps**: Secure webhook digestion and SHA-256 payload verification.

Submit your templates to our [GitHub Community Discussions](https://github.com/DevdeskApp/n8n-nodes-devdeskapp/discussions) to get featured in the official catalog!
