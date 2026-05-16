# MCP Protocol Test

Date: 2026-05-16

## Status

GO_MCP_PUBLIC_SAFE=true

Raw artifacts: `.tmp-public-safe-verify/`

## APIM Endpoint

Tested only through:

`https://apim-math-rag-mcp-5d67a258.azure-api.net/mcp`

## Results

- `/healthz`: 200, public-safe index counts 18,544 chunks / 104 sources
- `/readyz`: 200
- `initialize`: 200, `text/event-stream`, session ID present
- `notifications/initialized`: accepted
- `tools/list`: exactly `search`, `fetch`
- No `rag_*` tools visible
- No write tools visible
- Search responses expose `id`, `title`, `url`
- Fetch responses expose `id`, `title`, `text`, `url`, `metadata`
- `structuredContent` matches the JSON fallback in `content[0].text`

## Math Query Matrix

All 5 required queries returned nonzero results and fetch succeeded for the top
result:

1. `Apostolov Auvray Sektnan Poincare type toric metrics`
   - Top result: `Extremal Kähler Poincaré type metrics on toric varieties`
   - URL: `https://arxiv.org/abs/1711.08424`
2. `modified beta entropy e^F omega^n d1 approximation`
   - Top result: `Kahler metrics with cone singularities along a divisor`
   - URL: `https://arxiv.org/abs/1102.1196`
3. `weighted Mabuchi coercivity relative torus`
   - Top result: `Measures of finite energy in pluripotential theory: a synthetic approach`
   - URL: `https://arxiv.org/abs/2307.01697`
4. `Darvas Zhang quantization geodesic stability`
   - Top result: `A YTD correspondence for constant scalar curvature metrics`
   - URL: `https://arxiv.org/abs/2509.15173`
5. `Boucksom Jonsson weighted YTD`
   - Top result: `A YTD correspondence for constant scalar curvature metrics`
   - URL: `https://arxiv.org/abs/2509.15173`

## Latency Caveat

Search calls over the larger JSON index took about 30-32 seconds each through
APIM. This is functional but slow for interactive use. The likely cause is the
large JSON index and current low-cost Container Apps setup.

## Direct Backend Negative Controls

- Direct backend `/healthz`: 200, public-safe counts visible
- Direct backend `/readyz`: 200
- Direct backend `/mcp` without bearer: 401
- Direct backend `/mcp` with wrong bearer: 401

The direct backend remains publicly reachable, so this is not private-index
ready.
