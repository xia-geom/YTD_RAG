# Decision Log: Agent Logs Workflow

Date: 2026-05-04
Context: The project is developed with help from multiple coding agents, especially Codex and Claude Code. ChatGPT cannot directly access Codex or Claude Code chats.

Decision: Save important agent outputs into `agent_logs/` as curated Markdown files.

Reasoning: Agent final reports, reviews, test outputs, eval results, design decisions, limitations, and next-step recommendations are useful engineering memory. Storing them as Markdown makes them searchable through the existing local RAG/MCP system without scraping private agent chat state or depending on undocumented storage paths.

Alternatives Considered:
- Do nothing and rely on chat history. This fails because chat histories are not shared across tools.
- Store logs under `corpus/`. This risks mixing engineering memory with mathematical sources.
- Automatically scrape Codex or Claude Code logs. This is brittle and may expose private state unintentionally.

Consequences:
- `agent_logs/` is separate from `corpus/`.
- Agent logs are searchable engineering memory.
- Agent logs are not mathematical theorem evidence.
- Ingested chunks from `agent_logs/` are tagged with `source_kind: agent_log`.
- Users must manually curate what is saved.

Related Files:
- `agent_logs/README.md`
- `agent_logs/templates/agent_log_template.md`
- `agent_logs/templates/decision_log_template.md`
- `math_rag/src/math_rag/loaders.py`
- `math_rag/tests/test_loaders.py`

Follow-up Tasks:
- Save future Codex final reports under `agent_logs/codex/`.
- Save future Claude Code reviews under `agent_logs/claude/`.
- Periodically search logs for unresolved limitations and next-step recommendations.

## Evidence Boundary

This decision log is engineering memory only. Do not use it as mathematical theorem evidence.
