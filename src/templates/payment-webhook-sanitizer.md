---
title: 'Template #21376: Payment Webhook Sanitizer'
description: 'n8n template #21376: format payment webhook JSON, compute a SHA-256 checksum, add a UUID trace ID and audit slug, then route captured and failed payments to Slack.'
---

# 🛡️ Template #21376: Payment Webhook Sanitizer & Security Audit Pipeline

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io</span>
  <span class="badge-live badge-amber">Template ID: 21376</span>
</div>

🔗 **Template on n8n.io:** [n8n.io/workflows/21376](https://n8n.io/workflows/21376-sanitize-and-audit-payment-webhooks-with-devdeskapp-json-and-crypto-tools/)

<div class="doc-image">
  <img src="/images/fig-canvas-21376.png" alt="Template 21376 payment webhook sanitizer workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: The template on the n8n canvas.</div>

---

## 🎯 Overview

Payment gateways such as Stripe, Razorpay and Shopify send compact JSON webhooks that you want to log consistently, deduplicate and trace across systems. This template:

1. **Formats and validates** the raw body with the JSON Prettifier.
2. **Computes a SHA-256 checksum** of the formatted payload, a stable fingerprint for audit logs and deduplication.
3. **Adds a UUID v4 trace ID** for correlating the event across your database, logs and Slack.
4. **Builds an audit slug** from the order ID and customer name, for example `ord-89421-priya-patel`.
5. **Routes the event** with an If node: captured, valid payments go to a DevOps Slack alert, and anything else goes to a suspicious-transaction alert.

::: tip Checksum vs. signature verification
The SHA-256 here fingerprints the payload. It does **not** prove the webhook came from your gateway. To verify the gateway's signature header, add a DevDeskApp **E-Commerce & FinTech → Webhook Signature Verifier** node (HMAC-SHA256 for Razorpay, Shopify and Stripe) on the production webhook path.
:::

---

## 📸 Pipeline

<div class="doc-image">
  <img src="/images/fig-flow-21376.png" alt="Template 21376 pipeline: ingest, four DevDeskApp nodes, If gate, success and incident branches" />
</div>
<div class="doc-caption">Figure 2: Node order and branches in the published template.</div>

| Node | Type / operation | Purpose |
| :--- | :--- | :--- |
| Test workflow / Production Webhook Trigger | `manualTrigger` + sample Code node / `webhook` | Test with a sample `payment.captured` event, or receive live events |
| DevDeskApp: JSON Prettifier & Validator | `json` · `prettify` | Formats the raw body (string or object) |
| DevDeskApp: SHA-256 Integrity Hasher | `crypto` · `hash` (`sha256`) | Checksum of `formatted` |
| DevDeskApp: Trace UUID Generator | `crypto` · `uuid` | Trace ID |
| DevDeskApp: Audit Slug Normalizer | `text` · `slugify` | `orderId-customer` slug |
| If: Payment Captured & Valid | `if` | Splits success from incident |
| Format … Record / Alert + Slack | `code` + `slack` | Builds the audit record and posts the alert |

---

## ⚡ Audit record (from a real run of the sample event)

```json
{
  "status": "INGEST_AUTHENTICATED",
  "traceId": "78a2b9f9-b0b1-4061-8dab-a205441937d8",
  "auditSlug": "ord-89421-priya-patel",
  "event": "payment.captured",
  "paymentId": "pay_N982kls823a",
  "orderId": "ORD-89421",
  "customer": "Priya Patel",
  "amountFormatted": "₹4,999",
  "cryptographicProof": {
    "algorithm": "sha256",
    "payloadChecksum": "c87e5ce4d19729796b75ec57b8be2dd806a5af425f5f9d5abffd7741c2c41a21"
  },
  "databaseRecord": {
    "table": "audit_webhook_logs",
    "source": "payment_gateway_prod",
    "checksum": "c87e5ce4d19729796b75ec57b8be2dd806a5af425f5f9d5abffd7741c2c41a21"
  }
}
```

`traceId` changes on every run. The checksum stays the same for the same payload.

---

## 📥 Import it

1. Make sure `n8n-nodes-devdeskapp` is installed ([installation guide](/n8n/installation)).
2. Open the [template on n8n.io](https://n8n.io/workflows/21376-sanitize-and-audit-payment-webhooks-with-devdeskapp-json-and-crypto-tools/) and click **Use for free**, or copy the workflow JSON.
3. Paste it onto a new workflow canvas with **`Ctrl + V`** (**`Cmd + V`** on macOS).
4. Connect your **Slack** credentials and click **Test workflow**.
5. For production, register the **Production Webhook Trigger** URL in your payment gateway's webhook settings.
