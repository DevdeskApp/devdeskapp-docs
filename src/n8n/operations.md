---
title: 'n8n Node Operations Reference'
description: 'Reference for all 19 n8n-nodes-devdeskapp operations across 5 resources: parameters and real output fields for JSON, hashing, text, CTC payroll and e-commerce utilities.'
---
# Operations Reference

`n8n-nodes-devdeskapp` (latest: <NodeVersion />) gives you **one node with 5 resources and 19 operations**. Every operation runs synchronously inside your n8n process, makes no HTTP calls and returns one output item per input item (with `pairedItem` set).

<div class="doc-image">
  <img src="/images/fig-operations-map.png" alt="DevDeskApp node: 5 resources and 19 operations with their internal resource and operation values" />
</div>
<div class="doc-caption">Figure 1: Every resource and operation, with the internal values you see in workflow JSON.</div>

::: tip Where the examples come from
Every output below was produced by running the published node with the input shown. UUIDs are random on every run.
:::

---

## 1. JSON Utility (`json`)

All three operations read the **JSON Input** parameter (`jsonInput`, default `={{ $json }}`). It accepts a JSON string or an object from a previous node.

| Operation | Value | Extra parameter | Output fields |
| :--- | :--- | :--- | :--- |
| Prettify / Format | `prettify` | **Indentation** (`indentation`): `2`, `4` or `tab` (default `2`) | `formatted` (string), `success` |
| Minify | `minify` | none | `minified` (string), `success` |
| Validate | `validate` | none | `valid`, plus `parsed` (when valid) or `error` (when invalid) |

**Prettify** with input `{"status":"ok","code":200}`:

```json
{
  "formatted": "{\n  \"status\": \"ok\",\n  \"code\": 200\n}",
  "success": true
}
```

**Validate** with the invalid input `{"status":"ok",}`:

```json
{
  "valid": false,
  "error": "Expected double-quoted property name in JSON at position 15 (line 1 column 16)"
}
```

::: warning Invalid JSON in Prettify or Minify
Only **Validate** turns bad JSON into an output item. **Prettify** and **Minify** throw a `NodeOperationError` (`Invalid JSON input: ...`). Turn on **Settings → On Error → Continue** if you want those items to flow on as `{ "error": "..." }`.
:::

---

## 2. Crypto & Hash (`crypto`)

| Operation | Value | Parameters | Output fields |
| :--- | :--- | :--- | :--- |
| Hash (MD5 / SHA-256 / SHA-512) | `hash` | **Text/Payload** (`textPayload`), **Algorithm** (`hashAlgorithm`): `md5`, `sha1`, `sha256` (default), `sha512` | `algorithm`, `input`, `hash` (lowercase hex) |
| Base64 Encode | `base64Encode` | **Text/Payload** (`textPayload`) | `encoded`, `original` |
| Base64 Decode | `base64Decode` | **Text/Payload** (`textPayload`) | `decoded`, `original` |
| UUID V4 | `uuid` | none | `uuid`, `version` (`4`) |

**Hash**, SHA-256 of `devdeskapp`:

```json
{
  "algorithm": "sha256",
  "input": "devdeskapp",
  "hash": "3b7d21ca0cac379b91140262ad701f739f04f3dae19adf5ea04aa7e118fa50d3"
}
```

MD5 of `test@example.com` (the Gravatar-style lookup key) is `55502f40dc8b7c769880b10874abc9d0`.

**Base64 Encode** of `user:pass123`:

```json
{ "encoded": "dXNlcjpwYXNzMTIz", "original": "user:pass123" }
```

**UUID V4**:

```json
{ "uuid": "0f264685-868e-4cba-aab1-1b241c5f9c90", "version": 4 }
```

::: tip Hashing is not HMAC
`hash` is a plain digest of the text. To verify a signed webhook (a secret plus the body), use **E-Commerce & FinTech → Webhook Signature Verifier**, which computes HMAC-SHA256.
:::

---

## 3. Text & String (`text`)

All four operations read **Text Input** (`textInput`).

| Operation | Value | Extra parameter | Output fields |
| :--- | :--- | :--- | :--- |
| Slugify String | `slugify` | none | `original`, `slug` |
| Case Converter | `caseConverter` | **Target Case** (`targetCase`): `camelCase`, `kebabCase` (default), `lowerCase`, `pascalCase`, `snakeCase`, `upperCase` | `original`, `casing`, `result` |
| URL Encode | `urlEncode` | none | `original`, `encoded`, `success` |
| URL Decode | `urlDecode` | none | `original`, `decoded`, `success` (plus `error` if the input is malformed) |

**Slugify** of `Top 10 High-Growth AI Automation Trends in 2026! (Complete Guide)`:

```json
{
  "original": "Top 10 High-Growth AI Automation Trends in 2026! (Complete Guide)",
  "slug": "top-10-high-growth-ai-automation-trends-in-2026-complete-guide"
}
```

The slug is lowercased, characters other than letters, digits, spaces, `_` and `-` are removed, and runs of spaces, `_` or `-` become one `-`. There is no transliteration, so accented letters are dropped.

**Case Converter** of `DevDesk App Suite` to `snakeCase`:

```json
{ "original": "DevDesk App Suite", "casing": "snakeCase", "result": "dev_desk_app_suite" }
```

Words are split on spaces, punctuation and camel humps (`DevDesk` becomes `dev desk`). `upperCase` and `lowerCase` only change the letter case of the original string; they keep its spacing and punctuation.

::: danger Only the six listed Target Case values work
Values such as `lower`, `title` or `Title Case` are not supported. With them the node returns `"result": ""` without throwing an error. Read the converted text from `result`. There is no `convertedText` field.
:::

**URL Encode** of `hello world & foo=bar` returns `"encoded": "hello%20world%20%26%20foo%3Dbar"` (it uses JavaScript's `encodeURIComponent`).

---

## 4. HR & Calculator (`calculator`)

| Operation | Value | Parameters | Output fields |
| :--- | :--- | :--- | :--- |
| CTC to In-Hand Salary | `ctcToInHand` | **Annual CTC** (`annualCtc`, default `1200000`), **Basic Salary Percentage** (`basicPercentage`, default `50`) | `annualCtc`, `monthlyGross`, `monthlyInHand`, `breakdown{...}`, `taxRegime`, `reference` |

How the node calculates it:

- **Monthly basic** = CTC × basic % ÷ 12
- **Employee PF** = 12% of monthly basic, capped at **₹1,800**. Employer PF is the same.
- **Monthly gross** = (CTC − 12 × employer PF) ÷ 12
- **Professional tax** = flat ₹200 a month
- **Estimated TDS**: new-regime slabs after a ₹75,000 standard deduction (none at or below ₹7,00,000 CTC)
- **Monthly in-hand** = gross − employee PF − PT − TDS

**Annual CTC `1800000`, basic `50`:**

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

<div class="doc-image">
  <img src="/images/fig-ctc-output.png" alt="CTC to In-Hand Salary output for 18 lakh CTC: in-hand 1,28,075 of 1,48,200 monthly gross" />
</div>
<div class="doc-caption">Figure 2: Where the ₹1,48,200 monthly gross goes for a ₹18,00,000 CTC.</div>

More reference points (basic 50%):

| Annual CTC | Monthly gross | Est. TDS / month | Monthly in-hand |
| :--- | ---: | ---: | ---: |
| ₹12,00,000 | ₹98,200 | ₹6,563 | ₹89,638 |
| ₹18,00,000 | ₹1,48,200 | ₹18,125 | ₹1,28,075 |
| ₹24,00,000 | ₹1,98,200 | ₹33,125 | ₹1,63,075 |
| ₹28,00,000 | ₹2,31,533 | ₹43,125 | ₹1,86,408 |

::: warning Scope of the estimate
This is a quick benchmark, not a payroll engine. It does not model HRA or special allowance splits, the old tax regime, ESIC, cess, surcharge, rebates or state-specific professional tax. Field names are nested: use `breakdown.monthlyBasic` and `breakdown.employeePf`, not top-level `basicSalary` or `employeePf`.
:::

---

## 5. E-Commerce & FinTech (`ecommerce`)

| Operation | Value | Main parameters | Key output fields |
| :--- | :--- | :--- | :--- |
| Catalog Schema Mapper | `catalogMapper` | `sourcePlatform`, `targetPlatform` (Shopify, WooCommerce, Google Merchant Center), `catalogInput` | `items[]`, `totalItems` |
| Dynamic UPI QR & URI | `upiQr` | `payeeVpa`, `payeeName`, `amount`, `transactionRef`, `transactionNote`, `currency` | `upiUri`, `intentUrl` |
| GST JSON to Tabular Data | `gstJsonToTable` | `returnType` (`gstr1`, `gstr3b`, `gstr2b`), `gstSection` (`all`, `b2b`, `b2cs`), `gstJsonInput` | `rows[]`, `totalRows`, `totalTaxableValue`, `totalTax` |
| Profit Margin & ROAS Calculator | `profitCalculator` | `platform`, `sellingPrice`, `cogs`, `shippingFee`, `adSpend`, `rtoRatePct`, `commissionFeePct`, `closingFee`, `gstRatePct` | `netProfit`, `netMarginPct`, `breakEvenRoas`, `breakdown{...}` |
| Shipping Label Cropper Coordinates | `shippingLabelCrop` | `carrier`, `pageFormat`, `labelSize`, `thermalDpi` (`203` or `300`) | `cropBox{x,y,width,height}`, `dimensions`, `printableAreaPct` |
| Webhook Signature Verifier | `webhookVerifier` | `provider` (Razorpay, Shopify, Stripe, custom HMAC-SHA256), `webhookSecret`, `signatureHeader`, `rawBody`, `webhookEvent` | `verified`, `provider`, `event`, `error?` |
| WhatsApp Interactive Payload | `whatsappPayload` | `eventType`, `recipientPhone`, `headerText`, `bodyText`, `footerText`, `buttons` (max 3, 20 characters each) | `payload` (Meta Cloud API body), `buttonCount`, `metaApiEndpoint` |

**Dynamic UPI QR & URI** (`store@okaxis`, ₹499, ref `ORD-1042`):

```json
{
  "upiUri": "upi://pay?pa=store%40okaxis&pn=DevDesk+Store&am=499.00&tr=ORD-1042&tn=Order+1042&cu=INR",
  "amount": 499,
  "currency": "INR"
}
```

**Profit Margin & ROAS** (Amazon, price ₹999, COGS ₹350, shipping ₹60, ads ₹120, RTO 10%, commission 15%, closing fee ₹20, GST 18%):

```json
{
  "effectiveRevenue": 899.1,
  "netProfit": 183.88,
  "netMarginPct": 20.5,
  "breakEvenRoas": 2.38,
  "totalDeductions": 715.22
}
```

**Webhook Signature Verifier** (Razorpay, correct signature):

```json
{ "verified": true, "provider": "razorpay", "event": "payment.captured" }
```

Pass the **raw** request body. A re-serialised JSON object can differ byte for byte from what the gateway signed, and then `verified` is `false`. Razorpay and custom providers compare a hex HMAC, Shopify compares Base64, and Stripe reads `t=` and `v1=` from the header and signs `t.body`.

**Shipping Label Cropper** returns PDF point coordinates to crop from an A4 or Letter invoice. Flipkart on A4 at 203 DPI gives `cropBox: { "x": 24, "y": 448, "width": 547, "height": 370 }` and a 812 × 1218 px 4×6 label.

---

## Error handling

- Missing or invalid inputs that the node cannot process throw `NodeOperationError` with the item index.
- With **On Error → Continue (regular output)**, the failed item is returned as `{ "error": "<message>" }` and the remaining items keep going.
- Unsupported option values (for example a wrong `targetCase`) do **not** throw. Check outputs during testing.
