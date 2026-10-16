<script setup lang="ts">
interface NavCard {
  title: string
  category: string
  badge: string
  badgeType: 'emerald' | 'indigo' | 'purple' | 'amber' | 'cyan' | 'blue'
  description: string
  link: string
  linkText: string
  icon: string
  highlight?: boolean
}

const cards: NavCard[] = [
  {
    title: 'Getting Started',
    category: 'Architecture & Overview',
    badge: 'Core Concept',
    badgeType: 'indigo',
    description: 'Overview of DevDeskApp node, in-memory zero-latency execution, and security value proposition.',
    link: '/n8n/',
    linkText: 'n8n Overview',
    icon: '🚀'
  },
  {
    title: 'Installation Guide',
    category: 'Setup & Deployment',
    badge: 'UI & Docker',
    badgeType: 'cyan',
    description: 'Step-by-step setup via n8n Community Nodes UI, Docker container images, npm package, or environment variables.',
    link: '/n8n/installation',
    linkText: 'Installation Steps',
    icon: '📦'
  },
  {
    title: 'Operations Reference',
    category: 'Native Node Engine',
    badge: '10 Operations',
    badgeType: 'blue',
    description: 'Full schema specifications, input parameter types, and sample execution outputs for all 10 native operations.',
    link: '/n8n/operations',
    linkText: 'Operations Reference',
    icon: '⚙️'
  },
  {
    title: 'Workflow Templates',
    category: 'Official n8n.io Recipes',
    badge: 'Template #21017',
    badgeType: 'emerald',
    description: 'Explore official template #21017 published on n8n.io with pre-wired sample payloads and validation steps.',
    link: '/n8n/workflow-templates',
    linkText: 'Templates Guide',
    icon: '🌟',
    highlight: true
  },
  {
    title: 'Enterprise Architecture',
    category: 'Security & Benchmarks',
    badge: 'Zero-Leak Audit',
    badgeType: 'purple',
    description: 'Deep-dive security benchmarks comparing local native Node execution vs external cloud REST APIs.',
    link: '/solutions/',
    linkText: 'Architecture & Solutions',
    icon: '🛡️'
  },
  {
    title: 'Production Best Practices',
    category: 'Performance Tuning',
    badge: 'Optimization',
    badgeType: 'amber',
    description: 'High-throughput concurrency tips, memory management, defensive error handling, and automated CI/CD.',
    link: '/solutions/best-practices',
    linkText: 'Best Practices',
    icon: '⚡'
  }
]
</script>

<template>
  <div class="quick-nav-section">
    <div class="quick-nav-header">
      <div class="quick-nav-badge">
        <span class="pulse-dot" />
        <span>DOCUMENTATION HUB</span>
      </div>
      <h2 class="quick-nav-title">
        Explore the <span class="highlight-gradient">Knowledge Base</span>
      </h2>
      <p class="quick-nav-subtitle">
        Everything you need to build secure, sub-millisecond workflows with DevDeskApp. Select a guide to get started.
      </p>
    </div>

    <div class="quick-nav-grid">
      <a
        v-for="card in cards"
        :key="card.title"
        :href="card.link"
        class="nav-card"
        :class="{ 'is-highlighted': card.highlight }"
      >
        <div class="card-glow" />
        
        <div class="card-top">
          <div class="icon-bubble">
            <span class="icon-emoji">{{ card.icon }}</span>
          </div>
          <span class="card-badge" :class="`badge-${card.badgeType}`">
            {{ card.badge }}
          </span>
        </div>

        <div class="card-body">
          <div class="card-category">{{ card.category }}</div>
          <h3 class="card-title">{{ card.title }}</h3>
          <p class="card-desc">{{ card.description }}</p>
        </div>

        <div class="card-footer">
          <span class="link-label">{{ card.linkText }}</span>
          <span class="link-arrow">&rarr;</span>
        </div>
      </a>
    </div>
  </div>
</template>

<style scoped>
.quick-nav-section {
  position: relative;
  margin: 3.5rem 0 2rem 0;
}

.quick-nav-header {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 2.5rem auto;
}

.quick-nav-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 12px;
  border-radius: 9999px;
  background: rgba(99, 102, 241, 0.1);
  border: 1px solid rgba(99, 102, 241, 0.25);
  font-size: 0.72rem;
  font-weight: 700;
  color: #6366f1;
  letter-spacing: 0.08em;
  margin-bottom: 0.75rem;
}

.dark .quick-nav-badge {
  background: rgba(99, 102, 241, 0.15);
  border-color: rgba(99, 102, 241, 0.35);
  color: #818cf8;
}

.pulse-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: #6366f1;
  box-shadow: 0 0 8px #6366f1;
}

.dark .pulse-dot {
  background-color: #818cf8;
  box-shadow: 0 0 8px #818cf8;
}

.quick-nav-title {
  font-size: 1.85rem;
  font-weight: 800;
  line-height: 1.25;
  color: #0f172a;
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.02em;
}

.dark .quick-nav-title {
  color: #f8fafc;
}

.highlight-gradient {
  background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #38bdf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.quick-nav-subtitle {
  font-size: 0.98rem;
  color: #64748b;
  line-height: 1.55;
  margin: 0;
}

.dark .quick-nav-subtitle {
  color: #94a3b8;
}

/* 3-Column Responsive Grid */
.quick-nav-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}

/* Nav Card Styling */
.nav-card {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 1.5rem;
  border-radius: 16px;
  background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
  border: 1px solid #e2e8f0;
  text-decoration: none !important;
  color: inherit !important;
  box-shadow: 0 2px 8px -2px rgba(15, 23, 42, 0.05), 0 1px 3px rgba(15, 23, 42, 0.03);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
}

.dark .nav-card {
  background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%);
  border-color: #334155;
  box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
}

.nav-card:hover {
  transform: translateY(-4px);
  border-color: rgba(99, 102, 241, 0.5);
  box-shadow: 0 16px 32px -8px rgba(15, 23, 42, 0.12), 0 0 24px rgba(99, 102, 241, 0.18);
}

.dark .nav-card:hover {
  border-color: rgba(99, 102, 241, 0.55);
  box-shadow: 0 18px 36px -8px rgba(0, 0, 0, 0.65), 0 0 30px rgba(99, 102, 241, 0.22);
}

/* Subtle top gradient accent on hover */
.nav-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #6366f1, #a855f7, #38bdf8);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.nav-card:hover::before,
.nav-card.is-highlighted::before {
  opacity: 1;
}

/* Special highlight card for Template #21017 */
.nav-card.is-highlighted {
  border-color: rgba(16, 185, 129, 0.4);
}

.dark .nav-card.is-highlighted {
  border-color: rgba(16, 185, 129, 0.45);
}

.nav-card.is-highlighted:hover {
  border-color: #10b981;
  box-shadow: 0 18px 36px -8px rgba(0, 0, 0, 0.65), 0 0 30px rgba(16, 185, 129, 0.22);
}

/* Card Top Row */
.card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.1rem;
}

.icon-bubble {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: rgba(99, 102, 241, 0.08);
  border: 1px solid rgba(99, 102, 241, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.dark .icon-bubble {
  background: rgba(99, 102, 241, 0.15);
  border-color: rgba(99, 102, 241, 0.3);
}

.nav-card:hover .icon-bubble {
  transform: scale(1.1) rotate(4deg);
  background: rgba(99, 102, 241, 0.18);
  border-color: rgba(99, 102, 241, 0.45);
}

.icon-emoji {
  font-size: 1.35rem;
}

/* Badges */
.card-badge {
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 3px 8px;
  border-radius: 20px;
  white-space: nowrap;
}

.badge-emerald {
  background: rgba(16, 185, 129, 0.12);
  color: #10b981;
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.badge-indigo {
  background: rgba(99, 102, 241, 0.12);
  color: #6366f1;
  border: 1px solid rgba(99, 102, 241, 0.3);
}

.dark .badge-indigo {
  color: #818cf8;
}

.badge-purple {
  background: rgba(168, 85, 247, 0.12);
  color: #a855f7;
  border: 1px solid rgba(168, 85, 247, 0.3);
}

.badge-cyan {
  background: rgba(6, 182, 212, 0.12);
  color: #06b6d4;
  border: 1px solid rgba(6, 182, 212, 0.3);
}

.badge-blue {
  background: rgba(59, 130, 246, 0.12);
  color: #3b82f6;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.badge-amber {
  background: rgba(245, 158, 11, 0.12);
  color: #f59e0b;
  border: 1px solid rgba(245, 158, 11, 0.3);
}

/* Card Body */
.card-body {
  flex: 1;
}

.card-category {
  font-size: 0.72rem;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.3rem;
}

.dark .card-category {
  color: #94a3b8;
}

.card-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #0f172a;
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.01em;
  transition: color 0.2s ease;
}

.dark .card-title {
  color: #f8fafc;
}

.nav-card:hover .card-title {
  color: #6366f1;
}

.dark .nav-card:hover .card-title {
  color: #818cf8;
}

.card-desc {
  font-size: 0.88rem;
  color: #475569;
  line-height: 1.55;
  margin: 0;
}

.dark .card-desc {
  color: #94a3b8;
}

/* Card Footer */
.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 1.25rem;
  margin-top: 1.25rem;
  border-top: 1px solid #f1f5f9;
}

.dark .card-footer {
  border-top-color: #334155;
}

.link-label {
  font-size: 0.88rem;
  font-weight: 600;
  color: #6366f1;
  transition: color 0.2s ease;
}

.dark .link-label {
  color: #818cf8;
}

.link-arrow {
  font-size: 1.1rem;
  color: #6366f1;
  font-weight: 700;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.dark .link-arrow {
  color: #818cf8;
}

.nav-card:hover .link-arrow {
  transform: translateX(6px);
}

/* Responsive Breakpoints */
@media (max-width: 960px) {
  .quick-nav-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  .quick-nav-title {
    font-size: 1.6rem;
  }
}

@media (max-width: 640px) {
  .quick-nav-grid {
    grid-template-columns: 1fr;
    gap: 0.875rem;
  }
  .nav-card {
    padding: 1.25rem;
  }
  .quick-nav-title {
    font-size: 1.4rem;
  }
  .quick-nav-subtitle {
    font-size: 0.9rem;
  }
}
</style>
