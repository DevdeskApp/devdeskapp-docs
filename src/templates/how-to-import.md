---
title: 'How to Import n8n Templates'
description: 'Import the official DevDeskApp templates into n8n Cloud, self-hosted n8n or Docker by pasting the workflow JSON onto the canvas, step by step.'
---

# ⚡ How to Import Templates into n8n

You can import any workflow template built with **`n8n-nodes-devdeskapp`** into n8n Cloud, self-hosted n8n or Docker in under a minute.

<div class="doc-image">
  <img src="/images/fig-import-steps.png" alt="Three steps to import a DevDeskApp template: install the node, copy the template, paste on the canvas" />
</div>
<div class="doc-caption">Figure 1: Install the node once, then copy and paste any template.</div>

---

## Prerequisites

Install **`n8n-nodes-devdeskapp`** in your n8n instance first:

1. In n8n, open **Settings → Community Nodes**.
2. Click **Install**.
3. Enter `n8n-nodes-devdeskapp`, tick the risk acknowledgement and click **Install**.
4. On self-hosted n8n, community packages must be allowed (`N8N_COMMUNITY_PACKAGES_ENABLED=true`, the default).

See the [Installation Guide](/n8n/installation) for Docker, manual and queue-mode setups.

---

## 3-step import (copy and paste)

### Step 1: Open the template on n8n.io

| ID | Template | Extra credentials |
| :--- | :--- | :--- |
| #21017 | [Developer Suite & Security Engine](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities/) | None |
| #21130 | [CTC to In-Hand Salary Engine](https://n8n.io/workflows/21130-generate-indian-ctc-offers-and-payroll-breakdowns-with-devdeskapp/) | None |
| #21376 | [Payment Webhook Sanitizer](https://n8n.io/workflows/21376-sanitize-and-audit-payment-webhooks-with-devdeskapp-json-and-crypto-tools/) | Slack |
| #21593 | [AI LLM JSON Ingestion](https://n8n.io/workflows/21593-sanitize-and-ingest-ai-llm-json-into-postgres-with-devdeskapp-and-slack/) | PostgreSQL, Slack |
| #21594 | [CTC Offer Letter Generator](https://n8n.io/workflows/21594-generate-indian-ctc-offer-letters-with-devdeskapp-google-docs-gmail-and-slack/) | Google Docs, Gmail, Google Sheets, Slack |
| #21595 | [Meta CAPI Lead Sync](https://n8n.io/workflows/21595-hash-and-sync-leads-to-meta-capi-with-devdeskapp-google-sheets-and-slack/) | Meta access token, Google Sheets, Slack |
| #21596 | [Notion to WordPress Publisher](https://n8n.io/workflows/21596-publish-seo-safe-notion-blog-posts-to-wordpress-with-devdeskapp-and-slack/) | Notion, WordPress, Slack |

Click **Use for free** to open it in your own n8n, or use the copy option to put the workflow JSON on your clipboard.

::: warning Check the template page first
Templates #21593, #21594, #21595 and #21596 need a small fix after import. Each template page lists the exact change in its **Known issue** box.
:::

### Step 2: Open a canvas

1. Click **+** → **Workflow** in the n8n sidebar.
2. Click once on the empty canvas to focus it.

### Step 3: Paste

Press **`Ctrl + V`** (Windows / Linux) or **`Cmd + V`** (macOS). All nodes, sticky notes and connections appear on the canvas. Click **Test workflow** to run it.

---

## Troubleshooting

### Nodes show as unknown or with a question mark
- **Cause:** `n8n-nodes-devdeskapp` is not installed, or n8n has not reloaded since you installed it. n8n reports the node type `n8n-nodes-devdeskapp.devDeskApp` as not installed.
- **Fix:** Install the package from **Settings → Community Nodes**, reload the browser tab, and restart the container on Docker.

### Nothing happens on paste
- **Cause:** The canvas was not focused, or the clipboard holds the page URL instead of the workflow JSON.
- **Fix:** Click the canvas background and paste again. If you copied a link, open it and copy the workflow JSON.

### A node asks for credentials
- **Cause:** Templates #21376 and #21593 to #21596 use Slack, Google, Postgres, Notion, WordPress or Meta nodes.
- **Fix:** Open each highlighted node and choose or create the credential. The DevDeskApp nodes themselves never need credentials.
