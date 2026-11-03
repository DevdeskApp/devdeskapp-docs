---
title: 'Template #21130: CTC Salary Engine'
description: 'n8n template #21130: estimate Indian monthly in-hand pay from annual CTC with employee and employer PF, professional tax and TDS, then build an offer payload.'
---

# 💰 Template #21130: Employee CTC to In-Hand Salary Engine

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io</span>
  <span class="badge-live badge-green">Template ID: 21130</span>
  <span class="badge-live badge-blue">No credentials needed</span>
</div>

🔗 **Template on n8n.io:** [n8n.io/workflows/21130](https://n8n.io/workflows/21130-generate-indian-ctc-offers-and-payroll-breakdowns-with-devdeskapp/)

<div class="doc-image">
  <img src="/images/fig-canvas-21130.png" alt="Template 21130 CTC salary engine workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: The template on the n8n canvas.</div>

---

## 🎯 Overview

HR and recruiting teams often need a quick in-hand estimate while preparing an offer. This template takes a sample candidate (Arjun Sharma, Senior Cloud Architect, ₹18,00,000 CTC) through four DevDeskApp nodes:

1. **Candidate Slugifier** builds `arjun-sharma-senior-cloud-architect`.
2. **Indian CTC Payroll Engine** estimates monthly gross, PF, PT, TDS and in-hand pay.
3. **Offer Tracking UUID** creates the offer reference.
4. **Compensation Hasher** computes a SHA-256 of `name | CTC | in-hand` as a tamper check.

A Code node then assembles an offer and Slack-ready payload. Everything runs inside n8n with no external API calls.

---

## ⚙️ Parameter configuration

<div class="doc-image">
  <img src="/images/fig-ctc-parameters.png" alt="HR and Calculator node parameters: Annual CTC and Basic Salary Percentage, with the calculation steps" />
</div>
<div class="doc-caption">Figure 2: The two parameters of <strong>CTC to In-Hand Salary</strong> and how the node uses them.</div>

| Parameter | Internal name | Type | Node default | Value in this template |
| :--- | :--- | :--- | :--- | :--- |
| Annual CTC | `annualCtc` | Number | `1200000` | `1800000` (from the sample node) |
| Basic Salary Percentage | `basicPercentage` | Number | `50` | `50` (from the sample node) |

PF is always 12% of basic, capped at ₹1,800 a month, and professional tax is a flat ₹200. There are no switches to turn them off. See the [Operations Reference](/n8n/operations#_4-hr-calculator-calculator) for the full formula and its limits.

---

## 📊 Structured JSON output

<div class="doc-image">
  <img src="/images/fig-ctc-output.png" alt="CTC to In-Hand output for 18 lakh CTC: monthly in-hand 1,28,075" />
</div>
<div class="doc-caption">Figure 3: Real output of the payroll node for ₹18,00,000 CTC.</div>

```json
{
  "annualCtc": 1800000,
  "monthlyGross": 148200,
  "monthlyInHand": 128075,
  "breakdown": {
    "monthlyBasic": 75000,
    "employeePf": 1800,
    "employerPf": 1800,
    "professionalTax": 200,
    "estimatedMonthlyTds": 18125
  },
  "taxRegime": "India Standard / New Tax Benchmark",
  "reference": "https://www.devdeskapp.com/ctc-to-in-hand-calculator"
}
```

The final Code node turns this into a formatted offer payload, for example `"estimatedMonthlyInHandFormatted": "₹1,28,075"` and `"offerReferenceId": "OFFER-ARJUN-SHARMA-SENIO-83AF855D"`.

<div class="doc-image">
  <img src="/images/fig-ctc-executed.png" alt="Template 21130 after a successful test run with all nodes green" />
</div>
<div class="doc-caption">Figure 4: A successful test run, with every node green and 1 item per node.</div>

---

## 📥 Import it

1. Make sure `n8n-nodes-devdeskapp` is installed ([installation guide](/n8n/installation)).
2. Open the [template on n8n.io](https://n8n.io/workflows/21130-generate-indian-ctc-offers-and-payroll-breakdowns-with-devdeskapp/) and click **Use for free**, or copy the workflow JSON.
3. In n8n, paste it onto a new workflow canvas with **`Ctrl + V`** (**`Cmd + V`** on macOS).
4. Click **Test workflow**, then replace the sample node with your HRMS webhook, form or sheet.
