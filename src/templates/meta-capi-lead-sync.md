---
title: 'Template #21595: Meta CAPI Lead Hasher & Sync'
description: 'n8n template #21595: lowercase and SHA-256 hash lead emails with DevDeskApp, add a UUID event_id, send opted-in leads to the Meta Conversions API, log them to Google Sheets and alert Slack.'
---

# 📊 Template #21595: Hash and Sync Leads to Meta CAPI with DevDeskApp, Google Sheets, and Slack

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io</span>
  <span class="badge-live badge-purple">Template ID: 21595</span>
</div>

🔗 **Template on n8n.io:** [n8n.io/workflows/21595](https://n8n.io/workflows/21595-hash-and-sync-leads-to-meta-capi-with-devdeskapp-google-sheets-and-slack/)

<div class="doc-image">
  <img src="/images/fig-canvas-21595.png" alt="Template 21595 Meta CAPI lead sync workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: The template on the n8n canvas.</div>

---

## 🎯 Overview

The Meta Conversions API (CAPI) expects customer identifiers such as email to be **normalised (trimmed, lowercased) and SHA-256 hashed** before you send them. It also uses an `event_id` to deduplicate server events against pixel events. This template:

1. Trims and **lowercases** the lead email with DevDeskApp **Case Converter**.
2. **Hashes** it with SHA-256 in the n8n process, so the raw email is never sent to Meta.
3. Creates a **UUID v4 `event_id`** and a **campaign slug** such as `q4-enterprise-cloud-migration`.
4. Checks opt-in with an **If** node, then posts the event to the **Meta Graph API** (`/v19.0/{pixel_id}/events`), saves the lead to **Google Sheets** and alerts **Slack**. Leads without opt-in are logged to Slack and not sent.

Only the email is hashed. The phone number in the sample is not sent to Meta. If you need `ph`, add another hash node on the digits-only phone number.

::: danger Known issue in the published version (checked 4 Nov 2026)
As published, **every lead is sent with the same email hash**: `e3b0c442…b855`, the SHA-256 of an empty string. Meta cannot match these events. Fix two parameters after import:
1. **DevDeskApp: Email Lowercase & Clean**: set **Target Case** to **Lowercase** (`lowerCase`). The published value `lower` is not a valid option, so the node returns an empty `result`.
2. **DevDeskApp: SHA-256 Email Privacy Hasher**: set **Text/Payload** to `{{ $json.result }}`. The published `{{ $json.convertedText }}` refers to a field that does not exist.
:::

---

## 📸 Pipeline

<div class="doc-image">
  <img src="/images/fig-flow-21595.png" alt="Template 21595 pipeline: ingest, four DevDeskApp nodes, opt-in gate, Meta Graph API, Google Sheets and Slack" />
</div>
<div class="doc-caption">Figure 2: Node order and branches in the published template.</div>

| Node | Resource · Operation | Purpose |
| :--- | :--- | :--- |
| DevDeskApp: Email Lowercase & Clean | `text` · `caseConverter` (`lowerCase`) | Normalises `leadEmail.trim()` |
| DevDeskApp: SHA-256 Email Privacy Hasher | `crypto` · `hash` (`sha256`) | `em` value for CAPI |
| DevDeskApp: Event Deduplication UUID | `crypto` · `uuid` | `event_id` |
| DevDeskApp: Campaign Tracking Slug | `text` · `slugify` | Campaign tag in `custom_data` |
| If: Lead Has Opted-In & Verified Email | `if` | Only opted-in leads reach Meta |
| Meta Graph API: Dispatch Server CAPI Event | HTTP Request | `POST https://graph.facebook.com/v19.0/YOUR_PIXEL_ID/events` |

---

## ⚡ CAPI payload (with the fix above)

For the sample lead `user@example.com`, `Format Meta CAPI Payload` produces:

```json
{
  "data": [
    {
      "event_name": "Lead",
      "event_time": 1793735085,
      "event_id": "b7014673-4581-44c0-b06f-be1822754c7a",
      "user_data": {
        "em": ["b4c9a289323b21a01c3e940f150eb9b8c542587f1abfd8f0e1cc1ffc5e475514"]
      },
      "custom_data": {
        "currency": "INR",
        "value": 50000,
        "campaign": "q4-enterprise-cloud-migration"
      },
      "action_source": "system_generated"
    }
  ]
}
```

`b4c9a289…5514` is the SHA-256 of `user@example.com`. `event_id` and `event_time` change on every run.

---

## 📥 Import it

1. Make sure `n8n-nodes-devdeskapp` is installed ([installation guide](/n8n/installation)).
2. Open the [template on n8n.io](https://n8n.io/workflows/21595-hash-and-sync-leads-to-meta-capi-with-devdeskapp-google-sheets-and-slack/) and click **Use for free**, or copy the workflow JSON.
3. Paste it onto a new workflow canvas with **`Ctrl + V`** (**`Cmd + V`** on macOS).
4. Apply the two fixes from the known-issue box.
5. Replace `YOUR_PIXEL_ID`, add your Meta access token, and connect **Google Sheets** and **Slack** credentials.
6. Click **Test workflow** and check the event in Meta Events Manager → **Test events**.
