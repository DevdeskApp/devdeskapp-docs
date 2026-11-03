---
title: 'Production Best Practices'
description: 'Best practices for running n8n-nodes-devdeskapp in production: paired items, error handling with On Error, batch sizes, AI agent tools and safe hashing.'
---
# Production Best Practices

These practices help you run `n8n-nodes-devdeskapp` reliably in production workflows.

---

## 1. Reaching earlier data with paired items

n8n passes data between nodes as a list of items. Every item the DevDeskApp node returns carries **`pairedItem`** metadata that points back to the input item it came from:

```typescript
// Inside the node, for every input item i:
returnData.push({
  json: result,
  pairedItem: { item: i },
});
```

### Best practice
`$json` and `$input.item.json` only show the **previous** node's output. After a DevDeskApp node, that is the node's result (for example `{ "hash": "…" }`), not your original fields. To read a field from an earlier node, reference that node by name. n8n follows `pairedItem` back to the matching item:

```javascript
// In a later expression or Code node (Run Once for Each Item):
$('Webhook').item.json.body.candidateName
```

This works through a chain such as *Webhook → DevDeskApp Slugify → DevDeskApp Hash → Postgres*, because each DevDeskApp node keeps the pairing.

---

## 2. Error handling

If an item cannot be processed (for example invalid JSON in **Prettify**), the node throws a `NodeOperationError` linked to that item, and the execution stops:

```typescript
throw new NodeOperationError(this.getNode(), error, { itemIndex: i });
```

### Production recommendation
For batches from third parties where a few records may be malformed:

1. Open the DevDeskApp node and go to **Settings**.
2. Set **On Error** to **Continue** or **Continue (using error output)**.
3. Failed items are returned as `{ "error": "<message>" }` with the same `pairedItem`, and the remaining items keep going.
4. With **Continue (using error output)**, connect the node's error output to a Slack alert or a dead-letter table. With **Continue**, add an **If** node that checks whether `error` exists.

::: tip Use Validate when failures are expected
**JSON → Validate** never throws. It returns `valid: true/false` plus `error`, so you can branch on bad input without changing the error setting.
:::

---

## 3. Batch processing

The node's operations are synchronous and run in the n8n process with no network calls:

- **No rate limits.** You do not need **Loop Over Items** to avoid throttling. In a local benchmark, 10,000 items took about 13 ms for CTC, 23 ms for Prettify, 41 ms for Slugify and 46 ms for SHA-256 (node logic only, excluding n8n overhead).
- **Memory comes from your data.** Memory use grows with the size of the items you pass in. For very large or deeply nested payloads, split the input first so a single execution does not hold everything at once.

---

## 4. Using the node as an AI Agent tool

The node declares `usableAsTool: true`, so it can be attached to an n8n **AI Agent** as a tool.

### Setup steps
1. Add an **AI Agent** node and connect a chat model.
2. Click **+** on the agent's **Tool** input and add **DevDeskApp**.
3. Choose one resource and operation per tool node, for example **Calculator → CTC to In-Hand Salary** or **Crypto → Hash**.
4. Fill model-supplied inputs with `$fromAI()`, for example `{{ $fromAI('annualCtc', 'Annual CTC in rupees', 'number') }}`.
5. Tell the agent in its system prompt to call the tool for salary or hash questions instead of calculating.

On self-hosted n8n, set `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true` so community nodes can be used as tools.

<div class="doc-image">
  <img src="/images/fig-ai-agent-tool.png" alt="n8n AI Agent with DevDeskApp nodes attached to the Tool port" />
</div>
<div class="doc-caption">Figure 1: DevDeskApp nodes attached to an AI Agent's Tool port. More in <a href="/solutions/ai-agents">AI Agents & LLMs</a>.</div>

---

## 5. Hashing and secrets

- Use **SHA-256** or **SHA-512** for integrity checks and fingerprints. Reserve **MD5** and **SHA-1** for legacy lookups such as Gravatar.
- A plain hash is **not** a signature. To verify Razorpay, Shopify or Stripe webhooks, use **E-Commerce & FinTech → Webhook Signature Verifier**, which checks the provider's HMAC-SHA256 signature with your shared secret. Store that secret in a credential or environment variable, not in the workflow JSON.
- The **Hash** output includes the original `input`. Drop it with a **Set** node if the raw value must not travel further.
- The node makes no network calls and writes nothing to disk. n8n itself stores execution data, including inputs and outputs, according to your **execution saving** settings, so turn those down for workflows that handle secrets.
