# F32 Agentic MLOps Team

Standalone multi-agent reference architecture for controlled model delivery, release governance, observability, incident response, and rollback planning.

## Agent team

- Build Agent
- Registry Agent
- Release Agent
- Observability Agent
- Incident and Rollback Agent
- MLOps Orchestrator

The **actual specialist agent implementations live in [`src/agents.py`](src/agents.py)**. Shared run state and the release gate live in [`src/system.py`](src/system.py). Agent-composition and workflow tests live under [`tests/`](tests/).

## Architecture

```text
Build artifact
   ↓
Build Agent
   ↓
Registry Agent
   ↓
Release Agent
   ↓
Observability Agent
   ↓
Incident / Rollback Agent
   ↓
MLOps Orchestrator / Release Gate
```

The workflow treats build, registration, release, monitoring, incident readiness, and rollback as explicit operational artifacts. Release approval fails closed when required evidence is missing.

## Run

```bash
python -m src.run --example
pytest -q
```

**Maturity: Reference implementation.** It does not autonomously deploy production models or alter infrastructure.

## AI Engineering Handbook Series

By Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H

MIT licensed.
