# Agent Log: Project Structure Cleanup

Date: 2026-05-15
Agent: Codex
Branch: `codex/private-index-risk-accepted-pilot`
Commit: not created

## Status Before

The workspace contained several generated temporary directories at the repo
root and package root, plus many top-level MCP/Azure agent logs from earlier
pilot phases. Current source-of-truth MCP status logs were already present:

- `agent_logs/codex/2026-05-14-safe-fixture-chatgpt-harness.md`
- `agent_logs/codex/2026-05-15-mcp-connector-finalization.md`
- `agent_logs/codex/2026-05-15-private-real-index-risk-accepted-pilot.md`

## Goal

Reduce project structure noise while keeping useful engineering memory
recoverable.

## Files Moved

Local generated artifacts were moved to ignored local archive
`.archive/2026-05-15-local-cleanup/`:

- `.tmp-azure-deploy/`
- `.tmp-azure-test-index/`
- `.tmp-docker-test-index-auth/`
- `.tmp-fixture-verify/`
- `.pytest_cache/`
- `math_rag/.pytest_cache/` as `math_rag.pytest_cache/`
- `math_rag/build/` as `math_rag.build/`

Superseded MCP/Azure logs were moved to
`agent_logs/codex/archive/2026-05-15-mcp-history/`:

- `2026-05-07-azure-mcp-auth-review.md`
- `2026-05-07-azure-remote-mcp-prep.md`
- `2026-05-07-azure-tiny-pilot-final-status.md`
- `2026-05-07-azure-tiny-pilot.md`
- `2026-05-07-docker-remote-mcp-auth-gap-check.md`
- `2026-05-07-docker-remote-mcp-container-smoke-test.md`
- `2026-05-07-local-remote-mcp-smoke-test-helper.md`
- `2026-05-07-pre-azure-readiness.md`
- `2026-05-07-remote-mcp-app-auth.md`
- `2026-05-11-remote-streamable-http-mcp-server.md`
- `2026-05-12-low-cost-public-mcp.md`
- `2026-05-12-remote-mcp-apim-entra-fixture-pilot.md`
- `2026-05-12-remote-mcp-apim-pilot-multiagent.md`
- `2026-05-12-remote-mcp-chatgpt-connector-multiagent.md`
- `2026-05-12-remote-mcp-direct-ingress-hardening.md`
- `2026-05-12-remote-mcp-multiagent-plan.md`
- `2026-05-13-extended-verification-scope.md`
- `2026-05-13-remote-mcp-extended-verification.md`

## Files Created / Modified

- Added `.archive/` to `.gitignore`.
- Added `agent_logs/codex/archive/2026-05-15-mcp-history/README.md`.
- Added this cleanup log.

## Files Intentionally Not Moved

- `math_rag/src/**`
- `math_rag/tests/**`
- `deploy/azure/**`
- `docs/**`
- `findings/**`
- root docs
- `corpus/`
- `.math_rag_index/`
- `eval/`
- virtual environments
- `.env` files
- private research files

## Commands Run

```bash
git status --short
du -sh .tmp-* .pytest_cache math_rag/.pytest_cache math_rag/build 2>/dev/null
find agent_logs/codex -maxdepth 1 -type f -name '*.md' -print | sort
mkdir -p .archive/2026-05-15-local-cleanup
mv .tmp-azure-deploy .tmp-azure-test-index .tmp-docker-test-index-auth .tmp-fixture-verify .pytest_cache math_rag/.pytest_cache math_rag/build .archive/2026-05-15-local-cleanup/
mv math_rag/.pytest_cache .archive/2026-05-15-local-cleanup/math_rag.pytest_cache
mv .archive/2026-05-15-local-cleanup/build .archive/2026-05-15-local-cleanup/math_rag.build
mkdir -p agent_logs/codex/archive/2026-05-15-mcp-history
git mv <tracked superseded MCP/Azure logs> agent_logs/codex/archive/2026-05-15-mcp-history/
mv <untracked superseded MCP/Azure logs> agent_logs/codex/archive/2026-05-15-mcp-history/
find .archive/2026-05-15-local-cleanup -maxdepth 2 -type d | sort
find agent_logs/codex/archive/2026-05-15-mcp-history -maxdepth 1 -type f | sort
git diff --check
git diff --cached --check
```

The first local archive move partially completed before the package-local
`.pytest_cache` collided with the already-moved root `.pytest_cache`; the
package-local cache was then moved under the distinct name
`math_rag.pytest_cache`.

## Checks

Follow-up checks were run after the move:

```bash
find .archive/2026-05-15-local-cleanup -maxdepth 2 -type d | sort
find agent_logs/codex/archive/2026-05-15-mcp-history -maxdepth 1 -type f | sort
find . -maxdepth 2 -type d \( -name '.tmp-*' -o -name '.pytest_cache' -o -name 'build' \) -print | sort
```

The final find check showed no remaining top-level `.tmp-*`, `.pytest_cache`, or
`build` directories at max depth 2.

`git diff --cached --check` initially found one trailing whitespace line in an
archived historical log; it was normalized from `Bearer ` to `Bearer`, then both
unstaged and staged diff checks passed.

## Follow-Up Checklist

- Review whether `findings/` should remain top-level or move under `docs/` after
  the remote MCP release is cut.
- Review whether older non-MCP agent logs should be summarized or left as-is.
- Keep current MCP source-of-truth logs visible until the private-index lane is
  either completed or explicitly abandoned.

## Rollback

To restore local archived temp artifacts, move the desired directories back from
`.archive/2026-05-15-local-cleanup/`.

To restore a superseded log to the top-level Codex log folder, move it back from
`agent_logs/codex/archive/2026-05-15-mcp-history/` to `agent_logs/codex/`.

## Evidence Boundary

This log is engineering memory only. Do not use it as mathematical theorem
evidence.
