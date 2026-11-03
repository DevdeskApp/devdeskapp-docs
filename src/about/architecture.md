---
title: 'Architecture & Privacy'
description: 'How DevDeskApp keeps data local: tools that process input in the browser, and an n8n node that runs in-process with no external API calls.'
---
# Architecture & Privacy

DevDeskApp is built local-first. The web tools process your input in the browser, and the n8n node processes items inside your n8n instance. This page explains how each part handles data.

## Architectural model

<div class="doc-image">
  <img src="/images/fig-architecture.png" alt="DevDeskApp architecture: browser web app and the n8n community node, both processing data locally" />
</div>
<div class="doc-caption">Figure 1: Two products, one rule. The data you transform is processed where it already is.</div>

## Security and data isolation

### Web app (browser)
DevDeskApp Web is a Vue 3 single-page app, installable as a PWA.
1. **Tools run in the browser.** Formatters, encoders, hash generators and calculators process your input with JavaScript in the page. Your input is not sent to a DevDeskApp server.
2. **Some tools use the network by design.** Tools such as the API request tester or AI chat send the requests you ask them to send, because that is their job.
3. **Site analytics.** The site records page-view analytics to understand which tools are used. The tools do not send what you type into them.

### n8n community node
Calling an external utility API from an n8n **HTTP Request** node means:
- the provider's logs can capture customer records, PII and financial data,
- a provider outage breaks your workflow,
- rate limits drop items during peak load.

`n8n-nodes-devdeskapp` avoids all three. It runs synchronously in the n8n process that executes the workflow:
- Hashes use the Node.js `crypto` module (`createHash`, `randomUUID`).
- Text, JSON and casing operations are deterministic functions with no I/O.
- The CTC calculation is plain arithmetic with no network access.
- Every output item keeps `pairedItem`, so later nodes can reach the matching input item.

## Scalability and performance

Because the operations are pure, synchronous functions:
- **Throughput:** in a local benchmark, 10,000 items took 12.6 ms (CTC), 22.6 ms (Prettify), 40.7 ms (Slugify) and 46.5 ms (SHA-256) of node logic. See [Local vs Cloud](/solutions/).
- **Memory:** use scales with the size of the items you pass in. Nothing is cached between executions.
- **Deterministic results:** the same input and parameters always give the same output (UUID generation is the exception, by design). The node's test suite covers each operation.
