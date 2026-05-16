# ChatGPT Operator Check

Date: 2026-05-16

## Status

Manual ChatGPT operator check: pending.

## Reason

The APIM MCP endpoint is deployed and verified, but the ChatGPT web UI Draft app
step was not run from this environment.

## Operator Steps

1. In ChatGPT Developer Mode, create or refresh the connector with MCP URL:
   `https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp`
2. Use auth mode: `No Authentication`.
3. Confirm the visible tools are exactly:
   - `search`
   - `fetch`
4. Run:
   `Use the math_rag connector to search for Apostolov Auvray Sektnan Poincare type toric metrics. Fetch the most relevant result and summarize what the passage says, with caveats.`
5. Save a sanitized transcript showing:
   - ChatGPT used `search` first.
   - ChatGPT fetched one result.
   - No `rag_*` tools were visible.
   - No secrets, auth material, local paths, private notes, or raw private
     corpus markers appeared.

## Expected Result

The connector should be usable with `No Authentication` and should expose useful
public-safe math evidence from the deployed index.
