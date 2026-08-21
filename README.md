# F32 Agentic MLOps Team

Standalone multi-agent reference architecture for controlled model delivery, release governance, observability, incident response, and rollback planning.

## Agents
Build Agent, Registry Agent, Release Agent, Observability Agent, Incident and Rollback Agent, and MLOps Orchestrator.

The workflow treats build, registration, release, deployment readiness, monitoring, and rollback as explicit operational artifacts. Release approval fails closed when required evidence is missing.

## Run
```bash
python -m src.run --example
pytest -q
```

**Maturity: Reference implementation.** It does not autonomously deploy production models or alter infrastructure.

AI Engineering Handbook Series by Mahsa Keikha: https://a.co/d/0cbZnSMi and https://a.co/d/07HnRY7H

MIT licensed.
