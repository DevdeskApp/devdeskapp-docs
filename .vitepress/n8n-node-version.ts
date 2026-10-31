// Build-time n8n-nodes-devdeskapp version for the docs (Node only, used by config.mts).
// Order: npm registry -> ../n8n-nodes-devdeskapp/package.json (local dev) -> pinned fallback.
import fs from 'node:fs'
import path from 'node:path'
import { N8N_NODE_FALLBACK_VERSION, fetchLatestN8nNodeVersion, validVersion } from './theme/n8n-node'

export async function resolveN8nNodeVersion(): Promise<{ version: string; source: 'npm' | 'local' | 'fallback' }> {
  const fromNpm = await fetchLatestN8nNodeVersion()
  if (fromNpm) return { version: fromNpm, source: 'npm' }
  try {
    // process.cwd() is the docs repo root when running `vitepress build`.
    const pkg = JSON.parse(fs.readFileSync(path.resolve(process.cwd(), '..', 'n8n-nodes-devdeskapp', 'package.json'), 'utf8'))
    const local = validVersion(pkg.version)
    if (local) return { version: local, source: 'local' }
  } catch {}
  return { version: N8N_NODE_FALLBACK_VERSION, source: 'fallback' }
}
