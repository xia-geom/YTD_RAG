# Azure Deploy Result

Date: 2026-05-16

## Status

GO_AZURE_PUBLIC_SAFE_DEPLOYED=true

## Azure Resources Updated

- Resource group: `rg-math-rag-mcp-test`
- Storage account: `stmathragmcp5d67a258`
- New Azure Files share: `math-rag-public-safe-index`
- Container App: `math-rag-mcp-test`
- New active revision: `math-rag-mcp-test--0000003`

## Deployment

Uploaded only:

- `.math_rag_index/index.json`

Did not upload:

- `corpus/`
- PDFs
- `.env`
- raw source folders
- metadata enrichment cache
- secrets or credentials

The Container App still mounts the index at `/data/.math_rag_index`, but the
volume now points to environment storage `math-rag-public-safe-index`.

## Container App Status

- Provisioning state: `Succeeded`
- Running status: `Running`
- Latest revision: `math-rag-mcp-test--0000003`
- Latest ready revision: `math-rag-mcp-test--0000003`
- Storage mount: `/data/.math_rag_index`
- Storage name: `math-rag-public-safe-index`
- Access mode on environment storage: `ReadOnly`

APIM health after deployment:

- `/healthz`: 200
- `chunk_count`: 18,544
- `source_count`: 104
- `tool_mode`: `chatgpt`
- `tool_count`: 2

## Rollback

Restore the fixture mount by updating the Container App template volume
`storageName` from `math-rag-public-safe-index` back to
`math-rag-fixture-index`, then rerun APIM health and MCP smoke tests.
