# syntax=docker/dockerfile:1
#
# Build from the workspace root:
#   docker build -f deploy/azure/Dockerfile -t math-rag-remote-mcp:local .
#
# The root .dockerignore excludes corpus/, .math_rag_index/, PDFs, venvs, and secrets.

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV MATH_RAG_INDEX_DIR=/data/.math_rag_index
ENV MATH_RAG_REMOTE_MCP_READ_ONLY=true
ENV MATH_RAG_REMOTE_HOST=0.0.0.0
ENV MATH_RAG_REMOTE_PORT=8000
ENV MATH_RAG_REMOTE_TRANSPORT=http
ENV MATH_RAG_REMOTE_PATH=/mcp/

WORKDIR /app

RUN addgroup --system mathrag && adduser --system --ingroup mathrag mathrag

COPY math_rag/pyproject.toml math_rag/README.md /app/math_rag/
COPY math_rag/src /app/math_rag/src

RUN pip install --no-cache-dir "/app/math_rag[remote-mcp]"

USER mathrag

EXPOSE 8000

CMD ["python", "-m", "math_rag.remote_mcp_server"]
