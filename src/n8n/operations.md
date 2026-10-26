---
title: 'n8n Node Operations Reference'
description: 'Reference for every n8n-nodes-devdeskapp operation: inputs, options and output fields for JSON, hashing, UUID, encoding and payroll utilities.'
---
# Operations Reference

`n8n-nodes-devdeskapp` provides 4 resources with 13 deterministic operations. Every operation executes synchronously in-memory and outputs cleanly formatted JSON objects.

---

## 1. Crypto & Hash (`crypto`)

Generate cryptographic hashes for security tokens, Gravatar identifiers, cache keys, or payload integrity checks.

### Operations

#### MD5 Hash (`md5`)
Computes an MD5 hex digest from an input string.
- **Parameters**:
  - `Text to Hash` (`text`): The input string to hash.
- **Output JSON**:
  ```json
  {
    "input": "test@example.com",
    "hash": "55502f40dc8b7c769880b10874abc9d0",
    "algorithm": "md5"
  }
  ```

#### SHA-256 Hash (`sha256`)
Computes an industry-standard SHA-256 cryptographic digest.
- **Parameters**:
  - `Text to Hash` (`text`): The input string to hash.
- **Output JSON**:
  ```json
  {
    "input": "devdeskapp",
    "hash": "c0053e1a0673f4e3c35b80a1846b0a034f78de1f74075f782c5890772714041b",
    "algorithm": "sha256"
  }
  ```

#### SHA-512 Hash (`sha512`)
Computes a high-entropy SHA-512 cryptographic digest.
- **Parameters**:
  - `Text to Hash` (`text`): The input string to hash.
- **Output JSON**:
  ```json
  {
    "input": "devdeskapp",
    "hash": "9c12e52b2b1e2e...",
    "algorithm": "sha512"
  }
  ```

---

## 2. Text & String (`text`)

Perform string manipulation, casing conversion, and binary-to-text encoding.

### Operations

#### Convert String Case (`caseConverter`)
Transforms any string into the chosen formatting standard.
- **Parameters**:
  - `Text to Convert` (`text`): The input string.
  - `Target Case` (`targetCase`):
    - `camelCase` (e.g., `helloWorld`)
    - `kebab-case` (e.g., `hello-world`)
    - `lowercase` (e.g., `hello world`)
    - `PascalCase` (e.g., `HelloWorld`)
    - `Snake_Case` (e.g., `hello_world`)
    - `Title Case` (e.g., `Hello World`)
    - `UPPERCASE` (e.g., `HELLO WORLD`)
- **Output JSON**:
  ```json
  {
    "original": "DevDesk App Suite",
    "converted": "devdesk_app_suite",
    "case": "snakeCase"
  }
  ```

#### Base64 Encode String (`base64Encode`)
Encodes plaintext or raw strings into standard Base64.
- **Parameters**:
  - `Text to Encode` (`text`): Plaintext string.
- **Output JSON**:
  ```json
  {
    "original": "user:pass123",
    "encoded": "dXNlcjpwYXNzMTIz"
  }
  ```

#### Base64 Decode String (`base64Decode`)
Decodes Base64 encoded strings back to UTF-8 plaintext.
- **Parameters**:
  - `Base64 Text` (`text`): Valid Base64 string.
- **Output JSON**:
  ```json
  {
    "original": "dXNlcjpwYXNzMTIz",
    "decoded": "user:pass123"
  }
  ```

#### Url Encode String (`urlEncode`)
Encodes characters into percent-encoded URL formatting.
- **Parameters**:
  - `Text to Encode` (`text`): String with spaces or query characters.
- **Output JSON**:
  ```json
  {
    "original": "hello world & foo=bar",
    "encoded": "hello%20world%20%26%20foo%3Dbar"
  }
  ```

#### Url Decode String (`urlDecode`)
Decodes percent-encoded URL strings back into readable text.
- **Parameters**:
  - `URL Encoded Text` (`text`): Percent-encoded string.
- **Output JSON**:
  ```json
  {
    "original": "hello%20world%20%26%20foo%3Dbar",
    "decoded": "hello world & foo=bar"
  }
  ```

---

## 3. HR & Calculator (`hr`)

Compute comprehensive payroll, tax, and in-hand compensation models directly in n8n.

### Operations

#### Calculate In-Hand Salary (`inHandSalary`)
Breaks down annual Cost to Company (CTC) into statutory components:
- Basic salary, HRA, and Special Allowance.
- Employee deductions (EPF, ESIC, Professional Tax, estimated TDS).
- Employer contributions (Employer EPF, Gratuity, Insurance).
- Exact monthly and annual take-home (in-hand) pay.

- **Parameters**:
  - `Annual CTC (INR)` (`ctc`): Total annual compensation (e.g. `1200000`).
  - `Annual Bonus / Variable (INR)` (`bonus`): Optional bonus component (default: `0`).
  - `Metro City Resident` (`isMetro`): Boolean flag for HRA calculations (default: `true`).
  - `Income Tax Regime` (`taxRegime`): `new` (default) or `old`.
  - `Additional Custom Deductions (INR)` (`customDeductions`): Any extra annual deductions (default: `0`).

- **Output JSON Structure**:
  ```json
  {
    "annualCTC": 1200000,
    "bonus": 0,
    "taxRegime": "new",
    "isMetro": true,
    "monthlyGross": 100000,
    "monthlyInHand": 82600,
    "annualInHand": 991200,
    "breakdown": {
      "basicMonthly": 40000,
      "hraMonthly": 20000,
      "specialAllowanceMonthly": 40000,
      "employeePfMonthly": 1800,
      "professionalTaxMonthly": 200,
      "monthlyTaxEstimated": 15400
    }
  }
  ```

---

## 4. Utilities & Conversion (`utilities`)

High-speed system utilities for identity generation and workflow time stamping.

### Operations

#### Generate UUID V4 (`uuid`)
Generates a cryptographically random RFC 4122 Version 4 UUID.
- **Parameters**: None required.
- **Output JSON**:
  ```json
  {
    "uuid": "4f3b2a1c-9e8d-4a7b-8c5d-3e2f1a0b9c8d",
    "version": "v4"
  }
  ```

#### Current Timestamp & Unix Epoch (`timestamp`)
Generates timestamps in standard formats for file naming, database upserts, and time logging.
- **Parameters**: None required.
- **Output JSON**:
  ```json
  {
    "iso": "2026-10-15T18:30:00.000Z",
    "epochSeconds": 1792089000,
    "epochMillis": 1792089000000
  }
  ```
