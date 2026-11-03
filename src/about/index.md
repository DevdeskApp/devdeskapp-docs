---
title: 'About DevDeskApp'
description: 'What DevDeskApp is: a privacy-first suite of 340+ browser-based developer tools, plus an n8n community node that brings core utilities into your workflows.'
---
# About DevDeskApp

DevDeskApp is a developer productivity platform with **340+ browser-based tools** (formatters, encoders, generators and calculators), plus an open-source n8n community node that brings the most-used utilities into workflow automation.

## Mission

Every day, engineers and automation builders paste sensitive data into random online tools:
- connection strings and API payloads into online JSON formatters,
- passwords and tokens into third-party hash generators,
- salary figures into calculator websites.

DevDeskApp keeps that processing local:
1. **DevDeskApp Web** ([devdeskapp.com](https://www.devdeskapp.com/)): the tools process your input in your browser. It is not sent to a DevDeskApp server.
2. **n8n community node (`n8n-nodes-devdeskapp`)**: runs inside your n8n instance as plain Node.js code, with no external API calls and no third-party downtime.

---

## The DevDeskApp ecosystem

### 1. DevDeskApp Web
More than 340 tools, grouped for everyday work:
- **Formatters:** JSON, XML, HTML, CSS, SQL, YAML and more.
- **Crypto and security:** MD5, SHA-1, SHA-256, SHA-512, HMAC, JWT decoding, password generation.
- **Encoders and decoders:** Base64, URL, HTML entities, hex, Unicode.
- **Generators:** UUID, ULID, Lorem Ipsum, QR codes, dummy data.
- **Calculators and converters:** CTC to in-hand salary, gratuity, HR metrics, timestamps, units.

### 2. n8n community node
`n8n-nodes-devdeskapp` brings **19 operations** in 5 resources (JSON, Crypto, Text, Calculator, E-commerce) into n8n as typed form fields, so you can format payloads, hash fields, convert case and estimate salaries without writing Code nodes. See the [Operations Reference](/n8n/operations).

---

## Core principles

- **Privacy first:** the data you transform is processed where it already is, in your browser or your n8n instance.
- **Speed:** no network round trip for the processing itself.
- **Transparent maths:** calculators document their formulas. The CTC calculation shows the PF cap, PT and tax slabs it uses, and its output is an estimate.
- **Open source:** the n8n node is MIT licensed.
