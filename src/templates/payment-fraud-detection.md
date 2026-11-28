---
title: 'Template #22363: Payment Fraud Detection & Webhook Deduplication'
description: 'n8n template #22363: eliminate duplicate payment webhooks, compute zero-trust SHA-256 idempotency checksums, sanitize customer PII, and route fraud alerts to PostgreSQL and Slack.'
---

# 🛡️ Template #22363: Detect Payment Fraud and Deduplicate Webhooks with DevDeskApp, PostgreSQL, and Slack

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io</span>
  <span class="badge-live badge-red">Template ID: 22363</span>
</div>

🔗 **Template on n8n.io:** [n8n.io/workflows/22363](https://n8n.io/workflows/22363-detect-payment-fraud-and-deduplicate-webhooks-with-devdeskapp-postgresql-and-slack/)

<div class="doc-image">
  <img src="/images/fig-canvas-22363.png" alt="Template 22363 payment fraud detection and deduplication workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: The template on the n8n canvas.</div>

---

## 🎯 Overview

High-growth e-commerce platforms and SaaS businesses face two critical payment webhook challenges:
1. **Duplicate Webhook Retries**: Payment providers (Stripe, Razorpay, Shopify) retry delivery when servers take too long to reply, causing duplicate order fulfillments or duplicate digital credit top-ups.
2. **Fraudulent Chargebacks & Suspicious Orders**: High-ticket purchases made with disposable emails, proxy IPs, or mismatched billing addresses often slip through without automated risk scoring.

This template creates an automated zero-trust gate before fulfilling orders:

1. **Calculates SHA-256 Idempotency Checksum**: Hashes the transaction ID, currency, and amount with DevDeskApp **Hash Payload** into a deterministic key to instantly detect webhook replays.
2. **Issues Audit UUID v4**: Assigns a unique correlation token across PostgreSQL and ledger logs with DevDeskApp **UUID Generator**.
3. **PII Sanitization & Slugification**: Normalizes customer names and email domains into clean audit slugs (`order-8921-sarah-connor`) with DevDeskApp **Slugify String** without leaking raw PII.
4. **Automated Quarantine Gate**: Splits verified payments for instant database fulfillment, while quarantining suspicious orders into `#security-alerts` in Slack.

---

## 📸 Pipeline

<div class="doc-image">
  <img src="/images/fig-flow-22363.png" alt="Template 22363 pipeline: payment webhook, DevDeskApp hasher, UUID and slugifier, risk evaluation gate, Postgres and Slack branches" />
</div>
<div class="doc-caption">Figure 2: Node order and branches in the published template.</div>

| Node | Resource · Operation | Purpose |
| :--- | :--- | :--- |
| Payment Webhook (Stripe / Shopify) | `trigger` · `webhook` | Ingests live payment event (`charge.succeeded` or `payment_intent.succeeded`) |
| DevDeskApp: JSON Prettifier | `json` · `prettify` | Validates and cleans raw webhook JSON formatting |
| DevDeskApp: SHA-256 Idempotency Hasher | `crypto` · `hash` (`sha256`) | Checksum of `transactionId + amount` to prevent replay attacks |
| DevDeskApp: Trace UUID Generator | `crypto` · `uuid` | Distributed tracking ID across internal microservices |
| DevDeskApp: Customer Slugifier | `text` · `slugify` | Generates standardized order reference slug |
| If: Duplicate / High Risk? | `if` | Evaluates risk score, disposable email flag, and existing DB checksum |
| PostgreSQL: Ingest Order | Postgres node | Inserts verified payment record into production database |
| Slack: Security / Order Alert | Slack node | Alerts team of verified order or urgent fraud quarantine |

---

## ⚡ Execution sample

```json
{
  "status": "ORDER_VERIFIED",
  "auditToken": "8f2d5a1b-4c3e-4d9f-a6b8-2c7e1f4a9b0c",
  "orderSlug": "ord-98214-elena-rostova",
  "gateway": "stripe_live",
  "transactionId": "ch_3N82kls8921klsa",
  "amountFormatted": "$249.00 USD",
  "riskAssessment": {
    "riskScore": 12,
    "verdict": "LOW_RISK_ACCEPTED",
    "idempotencyHash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },
  "database": {
    "table": "ecommerce_orders",
    "inserted": true,
    "idempotencyKeyStored": true
  }
}
```

---

## 📥 Import it

1. Make sure `n8n-nodes-devdeskapp` is installed ([installation guide](/n8n/installation)).
2. Open the [template on n8n.io](https://n8n.io/workflows/22363-detect-payment-fraud-and-deduplicate-webhooks-with-devdeskapp-postgresql-and-slack/) and click **Use for free**, or copy the workflow JSON.
3. Paste it onto a new workflow canvas with **`Ctrl + V`** (**`Cmd + V`** on macOS).
4. Configure your **Stripe Webhook Secret**, **PostgreSQL connection**, and **Slack channel**.
5. Test using the sample webhook event and verify zero-delay in-memory checksum computation.
