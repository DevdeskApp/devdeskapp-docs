// n8n-nodes-devdeskapp version for the docs (browser-safe; also imported by the build).
//
// The build bakes the latest npm version into the HTML (.vitepress/n8n-node-version.ts),
// then <NodeVersion /> refreshes it in the browser so a new release shows up before the
// next docs deploy. The refresh runs at most once per CACHE_TTL_MS and only moves forward.
import { ref } from 'vue'

export const N8N_NODE_PACKAGE = 'n8n-nodes-devdeskapp'
export const N8N_NODE_NPM_URL = `https://www.npmjs.com/package/${N8N_NODE_PACKAGE}`
export const N8N_NODE_VERSIONS_URL = `${N8N_NODE_NPM_URL}?activeTab=versions`
export const N8N_NODE_REGISTRY_LATEST_URL = `https://registry.npmjs.org/${N8N_NODE_PACKAGE}/latest`
/** Used only when the registry and the sibling repo are both unavailable at build time. */
export const N8N_NODE_FALLBACK_VERSION = '0.1.6'

const SEMVER = /^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z.-]+))?(?:\+[0-9A-Za-z.-]+)?$/

export function validVersion(value: unknown): string | null {
  return typeof value === 'string' && SEMVER.test(value.trim()) ? value.trim() : null
}

/** Semver precedence: negative if a < b, 0 if equal, positive if a > b. */
export function compareVersions(a: string, b: string): number {
  const pa = SEMVER.exec(a)
  const pb = SEMVER.exec(b)
  if (!pa || !pb) return 0
  for (let i = 1; i <= 3; i++) {
    const diff = Number(pa[i]) - Number(pb[i])
    if (diff !== 0) return diff
  }
  if (!pa[4] !== !pb[4]) return pa[4] ? -1 : 1
  return (pa[4] || '').localeCompare(pb[4] || '', 'en', { numeric: true })
}

export async function fetchLatestN8nNodeVersion(timeoutMs = 5000): Promise<string | null> {
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort(), timeoutMs)
  try {
    const res = await fetch(N8N_NODE_REGISTRY_LATEST_URL, { signal: controller.signal })
    if (!res.ok) return null
    const body = await res.json()
    return validVersion(body?.version)
  } catch {
    return null
  } finally {
    clearTimeout(timer)
  }
}

// --- browser refresh ------------------------------------------------------------------
const CACHE_KEY = 'devdesk-docs:n8n-node-version'
const CACHE_TTL_MS = 6 * 60 * 60 * 1000
const version = ref('')
let refreshStarted = false

function apply(candidate: string | null) {
  if (candidate && (!version.value || compareVersions(candidate, version.value) > 0)) {
    version.value = candidate
  }
}

async function refresh() {
  try {
    const cached = JSON.parse(localStorage.getItem(CACHE_KEY) || 'null')
    if (cached && Date.now() - cached.at < CACHE_TTL_MS && validVersion(cached.version)) {
      apply(cached.version)
      return
    }
  } catch {}
  const latest = await fetchLatestN8nNodeVersion()
  if (!latest) return
  apply(latest)
  try {
    localStorage.setItem(CACHE_KEY, JSON.stringify({ version: latest, at: Date.now() }))
  } catch {}
}

/** Reactive version: starts at the build-time value, refreshed from npm once mounted. */
export function useN8nNodeVersion(buildVersion: string) {
  apply(validVersion(buildVersion))
  return version
}

/** Call from onMounted (client only). */
export function scheduleN8nNodeVersionRefresh() {
  if (refreshStarted || typeof window === 'undefined') return
  refreshStarted = true
  const idle = (window as Window & { requestIdleCallback?: (cb: () => void, opts?: { timeout: number }) => number }).requestIdleCallback
  if (idle) idle(() => { refresh() }, { timeout: 4000 })
  else setTimeout(() => { refresh() }, 2000)
}
