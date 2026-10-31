<script setup lang="ts">
import { ref } from 'vue'
import NodeVersion from './NodeVersion.vue'

const activeTab = ref<'json' | 'crypto' | 'ctc'>('json')

const tabs = [
  { id: 'json', label: '⚡ JSON Prettify', icon: '{ }' },
  { id: 'crypto', label: '🔐 SHA-256 Hash', icon: '#' },
  { id: 'ctc', label: '💼 CTC Calculator', icon: '₹' }
]
</script>

<template>
  <div class="hero-wrapper">
    <section class="hero-section">
      <!-- Geometric Radial Dot Grid -->
      <div class="hero-grid-bg" />

      <!-- Floating Ambient Glow Blobs -->
      <div class="hero-blob-1" />
      <div class="hero-blob-2" />
      <div class="hero-blob-3" />

      <div class="hero-inner">
        <!-- Left Column: Branding, Title, Actions, Metrics -->
        <div class="hero-col-left">
          <!-- DevDeskApp Eyebrow Badge -->
          <div class="hero-eyebrow-badge">
            <span class="pulse-ping">
              <span class="pulse-ping-ring"></span>
              <span class="pulse-ping-dot"></span>
            </span>
            <span class="badge-text-full">⚡ 330+ Tools • Official n8n Community Node • <NodeVersion /> Live</span>
            <span class="badge-text-short">⚡ 330+ Tools • n8n Node <NodeVersion /> Live</span>
          </div>

          <!-- Main Headline with DevDeskApp Gradient Shimmer -->
          <h1 class="hero-title">
            The Modern Automation &amp; <span class="hero-gradient-text">Developer Suite</span>
          </h1>

          <!-- Body Description -->
          <p class="hero-subtitle">
            Run <strong>330+ developer utilities</strong>, formatters, and financial calculation engines directly inside your
            <strong>n8n workflows</strong> with <span class="highlight-privacy">zero cloud data leaks</span> and sub-millisecond CPU speed.
          </p>

          <!-- Action Buttons -->
          <div class="hero-button-row">
            <a href="/n8n/" class="btn-primary-indigo">
              <span>🚀 n8n Node Guide</span>
              <span class="btn-arrow">&rarr;</span>
            </a>

            <div class="hero-button-subgroup">
              <a href="/n8n/operations" class="btn-secondary-slate">
                <span>📖 Operations</span>
              </a>

              <a
                href="https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities"
                target="_blank"
                rel="noopener"
                class="btn-template-highlight"
              >
                <span>🌟 Template #21017</span>
                <span class="badge-live-mini">Live</span>
              </a>
            </div>

            <a
              href="https://www.devdeskapp.com"
              target="_blank"
              rel="noopener"
              class="btn-web-suite"
            >
              <span>🌐 DevDeskApp Web Suite</span>
              <span class="btn-arrow">&rarr;</span>
            </a>
          </div>

          <!-- Metrics Strip -->
          <div class="metrics-strip">
            <div class="metric-box">
              <span class="metric-number">330+</span>
              <span class="metric-tag">Client Tools</span>
            </div>
            <div class="metric-sep"></div>
            <div class="metric-box">
              <span class="metric-number">&lt; 0.2ms</span>
              <span class="metric-tag">Execution Time</span>
            </div>
            <div class="metric-sep"></div>
            <div class="metric-box">
              <span class="metric-number">0 KB</span>
              <span class="metric-tag">Network Leak</span>
            </div>
            <div class="metric-sep"></div>
            <div class="metric-box">
              <span class="metric-number">100%</span>
              <span class="metric-tag">In-Memory Node</span>
            </div>
          </div>
        </div>

        <!-- Right Column: Interactive Code Sandbox Card -->
        <div class="hero-col-right">
          <div class="devdesk-terminal">
            <!-- Terminal Header -->
            <div class="terminal-topbar">
              <div class="mac-dots">
                <span class="dot red"></span>
                <span class="dot yellow"></span>
                <span class="dot green"></span>
              </div>
              <div class="terminal-center-title">
                <span>n8n Execution Sandbox</span>
              </div>
              <div class="speed-badge">
                <span class="check-icon">✓</span> 0.18ms
              </div>
            </div>

            <!-- Tab Switcher -->
            <div class="terminal-tabs">
              <button
                v-for="tab in tabs"
                :key="tab.id"
                :class="['term-tab-btn', { active: activeTab === tab.id }]"
                @click="activeTab = tab.id as any"
              >
                <span>{{ tab.label }}</span>
              </button>
            </div>

            <!-- Interactive Terminal Content -->
            <div class="terminal-body">
              <!-- Tab 1: JSON -->
              <div v-if="activeTab === 'json'" class="tab-content">
                <div class="term-comment">// Input: Minified Raw Webhook Payload</div>
                <div class="term-input">{"service":"payment","status":"success","empId":1042}</div>
                <div class="term-divider">
                  <span>⚡ DevDeskApp: JSON Prettifier</span>
                </div>
                <pre class="term-code"><code>{
  <span class="c-key">"service"</span>: <span class="c-str">"payment"</span>,
  <span class="c-key">"status"</span>: <span class="c-str">"success"</span>,
  <span class="c-key">"empId"</span>: <span class="c-num">1042</span>,
  <span class="c-key">"traceId"</span>: <span class="c-cyan">"8f2a1b9c-4e3d-4c8a-9f1e-2b3c4d5e6f7a"</span>
}</code></pre>
              </div>

              <!-- Tab 2: Crypto -->
              <div v-if="activeTab === 'crypto'" class="tab-content">
                <div class="term-comment">// Payload: Secret Verification Token</div>
                <div class="term-input">devdeskapp_production_webhook_secret_key</div>
                <div class="term-divider">
                  <span>🔐 DevDeskApp: SHA-256 Digest</span>
                </div>
                <pre class="term-code"><code>{
  <span class="c-key">"algorithm"</span>: <span class="c-str">"sha256"</span>,
  <span class="c-key">"hash"</span>: <span class="c-cyan">"c0053e1a0673f4e3c35b80a1846b0a034f78de1f74075f782c5890772714041b"</span>,
  <span class="c-key">"tamperProof"</span>: <span class="c-num">true</span>
}</code></pre>
              </div>

              <!-- Tab 3: CTC Calculator -->
              <div v-if="activeTab === 'ctc'" class="tab-content">
                <div class="term-comment">// Input: Annual Compensation Breakdown</div>
                <div class="term-input">annualCtc: ₹24,00,000 | basic: 50%</div>
                <div class="term-divider">
                  <span>💼 DevDeskApp: Indian Payroll Engine</span>
                </div>
                <pre class="term-code"><code>{
  <span class="c-key">"monthlyGross"</span>: <span class="c-num">₹2,00,000</span>,
  <span class="c-key">"takeHomeInHand"</span>: <span class="c-cyan">₹1,45,000</span>,
  <span class="c-key">"employeePf"</span>: <span class="c-num">₹12,000</span>,
  <span class="c-key">"professionalTax"</span>: <span class="c-num">₹200</span>
}</code></pre>
              </div>
            </div>

            <!-- Terminal Bottom Bar -->
            <div class="terminal-bottombar">
              <span class="status-live">● Synchronous Native Execution</span>
              <span class="status-sec">Zero External Network Calls</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.hero-wrapper {
  padding: 1.5rem 1rem 1rem 1rem;
  max-width: 1240px;
  margin: 0 auto;
}

.hero-section {
  position: relative;
  border-radius: 24px;
  overflow: hidden;
  padding: 3rem 2.5rem;
  border: 1px solid rgba(226, 232, 240, 0.8);
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(16px);
  box-shadow: 0 20px 40px -15px rgba(99, 102, 241, 0.06);
}

:global(.dark) .hero-section {
  border-color: rgba(51, 65, 85, 0.8);
  background: rgba(15, 23, 42, 0.6);
  box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.5);
}

/* Grid Background */
.hero-grid-bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: radial-gradient(circle at 1px 1px, rgba(99, 102, 241, 0.16) 1px, transparent 0);
  background-size: 28px 28px;
  mask-image: radial-gradient(ellipse at center, rgba(0, 0, 0, 1) 0%, rgba(0, 0, 0, 0) 75%);
  -webkit-mask-image: radial-gradient(ellipse at center, rgba(0, 0, 0, 1) 0%, rgba(0, 0, 0, 0) 75%);
  opacity: 0.7;
}

/* Floating Blobs */
.hero-blob-1 {
  position: absolute;
  top: -6rem;
  left: -6rem;
  width: 20rem;
  height: 20rem;
  border-radius: 9999px;
  background-color: rgba(99, 102, 241, 0.15);
  filter: blur(90px);
  pointer-events: none;
}

.hero-blob-2 {
  position: absolute;
  bottom: -6rem;
  right: -6rem;
  width: 20rem;
  height: 20rem;
  border-radius: 9999px;
  background-color: rgba(168, 85, 247, 0.15);
  filter: blur(90px);
  pointer-events: none;
}

.hero-blob-3 {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 24rem;
  height: 24rem;
  border-radius: 9999px;
  background-color: rgba(236, 72, 153, 0.08);
  filter: blur(110px);
  pointer-events: none;
}

:global(.dark) .hero-blob-1 { background-color: rgba(99, 102, 241, 0.22); }
:global(.dark) .hero-blob-2 { background-color: rgba(168, 85, 247, 0.2); }

/* Layout Grid */
.hero-inner {
  position: relative;
  z-index: 10;
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.95fr);
  gap: 2.75rem;
  align-items: center;
  width: 100%;
  box-sizing: border-box;
}

.hero-col-left {
  display: flex;
  flex-direction: column;
  gap: 1.15rem;
  min-width: 0;
  max-width: 100%;
  width: 100%;
  box-sizing: border-box;
}

/* Eyebrow Badge */
.hero-eyebrow-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border-radius: 9999px;
  border: 1px solid rgba(99, 102, 241, 0.3);
  background-color: rgba(99, 102, 241, 0.1);
  padding: 5px 14px;
  font-size: 0.78rem;
  font-weight: 700;
  color: #4f46e5;
  width: fit-content;
  max-width: 100%;
  backdrop-filter: blur(8px);
  box-shadow: 0 0 20px -3px rgba(99, 102, 241, 0.15);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.badge-text-short {
  display: none;
}

@media (max-width: 440px) {
  .badge-text-full {
    display: none;
  }
  .badge-text-short {
    display: inline;
  }
}

:global(.dark) .hero-eyebrow-badge {
  color: #818cf8;
}

.hero-eyebrow-badge:hover {
  transform: translateY(-1px) scale(1.02);
  box-shadow: 0 0 25px 0px rgba(99, 102, 241, 0.3);
}

/* Titles */
.hero-title {
  font-size: clamp(2.1rem, 3.8vw, 3.4rem);
  font-weight: 900;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: #0f172a;
  margin: 0;
}

:global(.dark) .hero-title {
  color: #f8fafc;
}

.hero-subtitle {
  font-size: clamp(0.95rem, 1.2vw, 1.1rem);
  line-height: 1.6;
  color: #475569;
  margin: 0;
  max-width: 580px;
}

:global(.dark) .hero-subtitle {
  color: #94a3b8;
}

.highlight-privacy {
  color: #0284c7;
  font-weight: 600;
}

:global(.dark) .highlight-privacy {
  color: #38bdf8;
}

/* Buttons */
.hero-button-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 0.5rem;
  align-items: center;
}

.hero-button-subgroup {
  display: flex;
  gap: 0.75rem;
  align-items: center;
}

.btn-primary-indigo {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  border-radius: 12px;
  background-color: #6366f1;
  color: #ffffff !important;
  font-size: 0.92rem;
  font-weight: 700;
  text-decoration: none !important;
  box-shadow: 0 4px 16px rgba(99, 102, 241, 0.35);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn-primary-indigo:hover {
  background-color: #4f46e5;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5);
}

.btn-arrow {
  transition: transform 0.2s ease;
}

.btn-primary-indigo:hover .btn-arrow {
  transform: translateX(3px);
}

.btn-secondary-slate {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 10px 16px;
  border-radius: 12px;
  background-color: #f1f5f9;
  color: #1e293b !important;
  border: 1px solid #e2e8f0;
  font-size: 0.92rem;
  font-weight: 600;
  text-decoration: none !important;
  transition: all 0.25s ease;
}

:global(.dark) .btn-secondary-slate {
  background-color: #1e293b;
  color: #f1f5f9 !important;
  border-color: #334155;
}

.btn-secondary-slate:hover {
  transform: translateY(-2px);
  background-color: #e2e8f0;
}

:global(.dark) .btn-secondary-slate:hover {
  background-color: #334155;
}

.btn-template-highlight {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border-radius: 12px;
  background-color: rgba(99, 102, 241, 0.08);
  color: #4f46e5 !important;
  border: 1px solid rgba(99, 102, 241, 0.3);
  font-size: 0.92rem;
  font-weight: 700;
  text-decoration: none !important;
  transition: all 0.25s ease;
}

:global(.dark) .btn-template-highlight {
  background-color: rgba(99, 102, 241, 0.15);
  color: #a5b4fc !important;
  border-color: rgba(99, 102, 241, 0.4);
}

.btn-template-highlight:hover {
  transform: translateY(-2px);
  background-color: rgba(99, 102, 241, 0.2);
}

.badge-live-mini {
  font-size: 0.68rem;
  font-weight: 800;
  background-color: #10b981;
  color: #ffffff;
  padding: 1px 6px;
  border-radius: 6px;
  text-transform: uppercase;
}

.btn-web-suite {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 10px 14px;
  border-radius: 12px;
  color: #64748b !important;
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none !important;
  transition: color 0.2s ease;
}

:global(.dark) .btn-web-suite {
  color: #94a3b8 !important;
}

.btn-web-suite:hover {
  color: #6366f1 !important;
}

/* Metrics Strip */
.metrics-strip {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding-top: 1.25rem;
  border-top: 1px solid #e2e8f0;
  margin-top: 0.5rem;
  flex-wrap: wrap;
}

:global(.dark) .metrics-strip {
  border-color: #334155;
}

.metric-box {
  display: flex;
  flex-direction: column;
}

.metric-number {
  font-size: 1.2rem;
  font-weight: 800;
  color: #0f172a;
}

:global(.dark) .metric-number {
  color: #f8fafc;
}

.metric-tag {
  font-size: 0.72rem;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.metric-sep {
  width: 1px;
  height: 26px;
  background-color: #e2e8f0;
}

:global(.dark) .metric-sep {
  background-color: #334155;
}

/* Right Column: Terminal Sandbox */
.hero-col-right {
  display: flex;
  justify-content: center;
  min-width: 0;
  max-width: 100%;
  width: 100%;
  box-sizing: border-box;
}

.devdesk-terminal {
  width: 100%;
  max-width: 500px;
  min-width: 0;
  box-sizing: border-box;
  background-color: #1e293b;
  border: 1px solid #334155;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.3), 0 0 25px rgba(99, 102, 241, 0.12);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
}

.devdesk-terminal:hover {
  transform: translateY(-3px);
  border-color: rgba(99, 102, 241, 0.5);
  box-shadow: 0 25px 50px -10px rgba(0, 0, 0, 0.4), 0 0 35px rgba(99, 102, 241, 0.2);
}

.terminal-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  background-color: #141e30;
  border-bottom: 1px solid #334155;
}

.mac-dots {
  display: flex;
  gap: 6px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.red { background-color: #ef4444; }
.yellow { background-color: #f59e0b; }
.green { background-color: #10b981; }

.terminal-center-title {
  font-size: 0.78rem;
  font-weight: 600;
  color: #94a3b8;
}

.speed-badge {
  font-size: 0.72rem;
  font-weight: 700;
  color: #34d399;
  background-color: rgba(52, 211, 153, 0.12);
  padding: 2px 7px;
  border-radius: 6px;
  border: 1px solid rgba(52, 211, 153, 0.3);
}

.check-icon {
  color: #34d399;
}

.terminal-tabs {
  display: flex;
  background-color: #0f172a;
  border-bottom: 1px solid #334155;
  padding: 4px;
  gap: 4px;
}

.term-tab-btn {
  flex: 1;
  background: transparent;
  border: none;
  color: #94a3b8;
  padding: 6px 8px;
  font-size: 0.78rem;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.term-tab-btn:hover {
  color: #f8fafc;
  background-color: rgba(255, 255, 255, 0.05);
}

.term-tab-btn.active {
  background-color: #1e293b;
  color: #818cf8;
  border: 1px solid #334155;
}

.terminal-body {
  padding: 16px;
  font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
  font-size: 0.83rem;
  min-height: 220px;
  background-color: #141e30;
}

.tab-content {
  animation: fadeIn 0.25s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(3px); }
  to { opacity: 1; transform: translateY(0); }
}

.term-comment {
  color: #64748b;
  font-size: 0.75rem;
  margin-bottom: 6px;
}

.term-input {
  color: #cbd5e1;
  background-color: #0f172a;
  padding: 6px 10px;
  border-radius: 6px;
  margin-bottom: 10px;
  font-size: 0.78rem;
  border-left: 2px solid #6366f1;
  overflow-x: auto;
  white-space: pre-wrap;
  word-break: break-all;
  max-width: 100%;
}

.term-divider {
  display: flex;
  align-items: center;
  color: #818cf8;
  font-size: 0.74rem;
  font-weight: 700;
  margin: 8px 0;
  letter-spacing: 0.03em;
}

.term-code {
  background: transparent !important;
  padding: 0 !important;
  margin: 0 !important;
  overflow-x: auto;
  color: #f8fafc;
  line-height: 1.5;
  max-width: 100%;
  white-space: pre;
}

.term-code code {
  max-width: 100%;
}

.c-key { color: #f472b6; }
.c-str { color: #34d399; }
.c-num { color: #fbbf24; }
.c-cyan { color: #38bdf8; font-weight: 600; }

.terminal-bottombar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 14px;
  background-color: #0f172a;
  border-top: 1px solid #334155;
  font-size: 0.72rem;
  color: #64748b;
}

.status-live {
  color: #10b981;
}

/* RESPONSIVE DESIGN (Tablets & Medium Screens) */
@media (max-width: 1024px) {
  .hero-inner {
    grid-template-columns: 1fr;
    gap: 2.25rem;
  }

  .hero-section {
    padding: 2.25rem 1.75rem;
    border-radius: 20px;
  }

  .devdesk-terminal {
    max-width: 100%;
  }

  .hero-title {
    font-size: clamp(2rem, 4vw, 2.6rem);
  }

  .metrics-strip {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
  }

  .metric-sep {
    display: none;
  }
}

@media (min-width: 641px) and (max-width: 900px) {
  .hero-button-row {
    display: flex;
    flex-direction: column;
    width: 100%;
    gap: 0.75rem;
  }

  .hero-button-subgroup {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
    width: 100%;
  }

  .btn-primary-indigo,
  .btn-secondary-slate,
  .btn-template-highlight,
  .btn-web-suite {
    width: 100%;
    justify-content: center;
  }
}

/* RESPONSIVE DESIGN (Mobile Phones <= 640px) */
@media (max-width: 640px) {
  .hero-wrapper {
    padding: 0.5rem 0.25rem;
    width: 100%;
    box-sizing: border-box;
    overflow-x: hidden;
  }

  .hero-section {
    padding: 1.25rem 0.875rem;
    border-radius: 16px;
    width: 100%;
    box-sizing: border-box;
    overflow: hidden;
  }

  .hero-inner {
    grid-template-columns: minmax(0, 1fr);
    gap: 1.5rem;
    width: 100%;
    box-sizing: border-box;
  }

  .hero-col-left,
  .hero-col-right {
    min-width: 0;
    max-width: 100%;
    width: 100%;
    box-sizing: border-box;
  }

  .hero-eyebrow-badge {
    font-size: 0.72rem;
    padding: 4px 10px;
    line-height: 1.4;
    white-space: normal;
    text-align: left;
    max-width: 100%;
    box-sizing: border-box;
  }

  .hero-title {
    font-size: clamp(1.6rem, 5.8vw, 2.1rem);
    line-height: 1.2;
    word-break: break-word;
  }

  .hero-subtitle {
    font-size: 0.9rem;
    line-height: 1.55;
    word-break: break-word;
  }

  .hero-button-row {
    display: flex;
    flex-direction: column;
    width: 100%;
    gap: 0.65rem;
    box-sizing: border-box;
  }

  .btn-primary-indigo {
    width: 100%;
    justify-content: center;
    font-size: 0.92rem;
    padding: 11px 16px;
    min-height: 44px;
    box-sizing: border-box;
  }

  .hero-button-subgroup {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.5rem;
    width: 100%;
    box-sizing: border-box;
  }

  .btn-secondary-slate,
  .btn-template-highlight {
    width: 100%;
    justify-content: center;
    font-size: 0.82rem;
    padding: 10px 6px;
    min-height: 44px;
    box-sizing: border-box;
    text-align: center;
    gap: 4px;
  }

  .badge-live-mini {
    font-size: 0.62rem;
    padding: 1px 4px;
  }

  .btn-web-suite {
    width: 100%;
    justify-content: center;
    font-size: 0.85rem;
    padding: 8px 12px;
    box-sizing: border-box;
  }

  /* 2x2 Clean Grid on Mobile for Metrics */
  .metrics-strip {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 8px !important;
    width: 100%;
    box-sizing: border-box;
    padding-top: 1rem;
  }

  .metric-box {
    background: rgba(99, 102, 241, 0.05);
    border: 1px solid rgba(99, 102, 241, 0.15);
    border-radius: 12px;
    padding: 10px 8px;
    text-align: center;
    align-items: center;
    box-sizing: border-box;
    min-width: 0;
  }

  :global(.dark) .metric-box {
    background: rgba(30, 41, 59, 0.6);
    border-color: rgba(51, 65, 85, 0.8);
  }

  .metric-number {
    font-size: 1.15rem;
    font-weight: 800;
  }

  .metric-tag {
    font-size: 0.65rem;
    font-weight: 600;
    white-space: nowrap;
  }

  .metric-sep {
    display: none;
  }

  /* Terminal Mobile Adjustments */
  .devdesk-terminal {
    border-radius: 14px;
    width: 100%;
    min-width: 0;
    box-sizing: border-box;
  }

  .terminal-topbar {
    padding: 8px 10px;
    box-sizing: border-box;
  }

  .terminal-center-title {
    font-size: 0.72rem;
  }

  .speed-badge {
    font-size: 0.68rem;
    padding: 2px 6px;
  }

  .terminal-tabs {
    flex-wrap: nowrap;
    overflow-x: auto;
    padding: 3px;
    box-sizing: border-box;
  }

  .term-tab-btn {
    white-space: nowrap;
    font-size: 0.7rem;
    padding: 5px 6px;
    flex: none;
  }

  .terminal-body {
    padding: 10px;
    font-size: 0.74rem;
    min-height: 170px;
    box-sizing: border-box;
    overflow-x: auto;
  }

  .term-input {
    font-size: 0.7rem;
    padding: 5px 6px;
    white-space: pre-wrap;
    word-break: break-all;
  }

  .terminal-bottombar {
    flex-direction: column;
    gap: 4px;
    align-items: flex-start;
    padding: 8px 10px;
    font-size: 0.68rem;
    box-sizing: border-box;
  }
}

@media (max-width: 360px) {
  .hero-button-subgroup {
    grid-template-columns: 1fr;
  }
}
</style>
