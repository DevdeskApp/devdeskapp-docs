---
title: 'Architecture & Privacy'
description: 'How DevDeskApp keeps data private: client-side processing in the browser and in-memory execution inside n8n, with no payloads sent to external servers.'
---
# Architecture & Privacy

DevDeskApp is engineered around a strict local-first and privacy-first architectural paradigm. This document explains how the web platform and automation nodes handle memory, security, and execution isolation.

## Architectural Model

```
+-------------------------------------------------------------+
|                      DevDeskApp Suite                       |
+------------------------------+------------------------------+
|       DevDeskApp Web         |     n8n-nodes-devdeskapp     |
|   (Browser / Vue 3 + PWA)    |    (n8n In-Process Engine)   |
+------------------------------+------------------------------+
|  * 100% Client-Side V8       |  * Native Node.js Execution  |
|  * Web Crypto API (Subtle)   |  * Node.js crypto module     |
|  * Zero Network Roundtrips   |  * zero external HTTP calls  |
|  * IndexedDB Local Caching   |  * Sub-millisecond latency   |
|  * Offline Service Worker    |  * pairedItem lineage        |
+------------------------------+------------------------------+
```

## Security & Data Isolation

### Client-Side Execution (Web)
When you paste an API secret, JSON structure, or salary value into DevDeskApp Web:
1. **No Outbound Network Requests**: The browser makes no network requests for data processing. All computations take place inside the client V8 engine.
2. **Web Crypto Standards**: Hashing and cryptographic transforms leverage the browser native `crypto.subtle` API for hardware-accelerated, timing-attack-resistant security.
3. **No Third-Party Analytics on Payloads**: DevDeskApp does not log, inspect, or retain input strings. Refreshing the browser or clearing tab memory clears all transient computation data.

### In-Process Execution (n8n Community Node)
In enterprise automation workflows, data leakage often occurs when teams call external SaaS APIs (like cloud text formatters or public hash APIs) inside n8n HTTP Request nodes:
- External API logs capture your customer records, PII, and financial parameters.
- Cloud outages break business-critical workflows.
- API rate limits cause automation drops during peak hours.

The `n8n-nodes-devdeskapp` node executes synchronously within the active Node.js event loop of your n8n workflow execution container:
- Uses Node.js native `crypto` module (`createHash`) for cryptographic hashes.
- Performs string manipulations and casing algorithms with deterministic pure functions.
- Processes Indian CTC calculations with zero network connectivity.

## Scalability & Performance

Because operations are synchronous pure functions without I/O blocking:
- **Throughput**: Capable of processing tens of thousands of items per second in n8n batch loops.
- **Memory Footprint**: Transient object allocations are immediately garbage-collected by V8.
- **Deterministic Results**: Unit-tested with 100% branch test coverage across standard test suites.
