---
title: 'AI Agents & LLM Function Calling'
description: 'Attach the DevDeskApp node to an n8n AI Agent as a tool, so the model calls it for exact CTC maths, SHA-256 hashes and JSON formatting instead of guessing.'
---

# 🤖 AI Agents & LLM Function Calling

The DevDeskApp node declares `usableAsTool: true`, so you can attach it to the **Tool** port of an n8n **AI Agent**. The model decides *when* to call it, and the node does the actual work: salary maths, hashing, encoding and JSON formatting. This works with any chat model n8n supports, such as OpenAI, Anthropic, Google Gemini or Ollama.

---

## 🌟 Why give an agent DevDeskApp tools?

1. **Exact maths.** LLMs often get multi-step payroll arithmetic wrong (PF caps, tax slabs, rounding). The CTC operation returns the same numbers every time.
2. **Exact strings.** A model cannot compute a SHA-256 hash, Base64 or a UUID in its head. It will invent something that looks right.
3. **Smaller prompts.** Minifying a large JSON payload before it goes into the prompt removes indentation and line breaks, which saves tokens.

The node runs inside your n8n process and makes no network calls of its own. Data you pass to the **chat model**, though, still goes to that model's provider. Hash or strip sensitive fields *before* they reach the agent if they must not leave your instance.

---

## 📸 Architecture: AI Agent with DevDeskApp tools

<div class="doc-image">
  <img src="/images/fig-ai-agent-tool.png" alt="n8n AI Agent with a chat model and DevDeskApp nodes attached to the Tool port" />
</div>
<div class="doc-caption">Figure 1: The agent receives a chat message, the model chooses a tool, and the DevDeskApp node returns an exact result.</div>

---

## 🎯 Use cases

### 1. 🧮 Salary questions (CTC to in-hand)

Prompt: *"What is the monthly take-home and employee PF for a ₹24,00,000 CTC?"*

The agent calls the DevDeskApp tool set to **Calculator → CTC to In-Hand Salary** with `annualCtc = 2400000`, and the node returns:

```json
{
  "annualCtc": 2400000,
  "monthlyGross": 198200,
  "monthlyInHand": 163075,
  "breakdown": {
    "monthlyBasic": 100000,
    "employeePf": 1800,
    "employerPf": 1800,
    "professionalTax": 200,
    "estimatedMonthlyTds": 33125
  },
  "taxRegime": "India Standard / New Tax Benchmark",
  "reference": "https://www.devdeskapp.com/ctc-to-in-hand-calculator"
}
```

The agent then answers with **₹1,63,075 in hand per month** and **₹1,800 employee PF**. PF is 12% of basic, capped at ₹1,800, and TDS uses the new-regime slabs with the ₹75,000 standard deduction. Treat the output as an estimate, not payroll advice. See the [Operations Reference](/n8n/operations#_4-hr-calculator-calculator) for the full formula.

### 2. 🧹 Shrinking JSON before it reaches the model

Put a DevDeskApp node set to **JSON → Minify** *before* the agent, as a normal step rather than a tool, and pass its `minified` output into the prompt. Removing whitespace from a pretty-printed payload usually cuts its size noticeably. The exact saving depends on how indented the input was.

### 3. 🔐 Hashing identifiers

Ask the agent to fingerprint a value, or hash IDs before the agent sees them. **Crypto → Hash** with `sha256` returns, for example:

```json
{ "algorithm": "sha256", "input": "devdeskapp", "hash": "3b7d21ca0cac379b91140262ad701f739f04f3dae19adf5ea04aa7e118fa50d3" }
```

The output echoes `input`. If the raw value is sensitive, remove `input` with a **Set** node before passing the result on.

---

## ⚙️ Setup in n8n

### Step 1: Add the agent and a chat model
1. Add a **When chat message received** trigger and an **AI Agent** node.
2. Connect a chat model (for example **OpenAI Chat Model**, **Anthropic Chat Model** or **Ollama Chat Model**) to the agent's **Chat Model** input.

### Step 2: Attach DevDeskApp as a tool
1. Click **+** on the agent's **Tool** input and search for **DevDeskApp**.
2. Pick the **Resource** and **Operation**, for example **Calculator → CTC to In-Hand Salary**. Each tool node runs one operation, so add one node per tool you want to offer (CTC, Hash, Minify and so on).
3. Give each tool a clear name and description, such as *"Calculates Indian monthly in-hand salary from annual CTC in rupees"*. The model uses this text to decide when to call it.
4. For inputs the model should fill in, use `$fromAI()` in the parameter, for example **Annual CTC** = `{{ $fromAI('annualCtc', 'Annual CTC in rupees', 'number') }}`.

::: tip Self-hosted n8n
For community nodes to appear as agent tools on self-hosted n8n, set the environment variable `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true` and restart n8n.
:::

### Step 3: System prompt

```markdown
You can call DevDeskApp tools.
- For any salary, PF, professional tax or take-home question, call the CTC tool. Never calculate it yourself.
- For hashes, Base64 or UUIDs, call the matching DevDeskApp tool and return its exact output.
- Quote numbers exactly as the tool returns them.
```

---

## 🚀 Next steps

- See all 19 operations in the [Operations Reference](/n8n/operations).
- Compare local and cloud execution in [Enterprise Architecture](/solutions/).
- Start from a ready workflow in [Workflow Templates](/n8n/workflow-templates).
