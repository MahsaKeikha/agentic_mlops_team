# F32 Agentic MLOps Team

Standalone multi-agent reference architecture for controlled model delivery, release governance, observability, incident response, and rollback planning.

## Architecture

```text
src/
├── agents/          Build, Registry, Release, Observability, Incident/Rollback agents
├── tools/           deterministic MLOps inspection and planning helpers
├── skills/          reusable release and reliability procedures
├── memory/          release-event memory
├── schemas/         release evidence contracts
├── prompts/         operational principles
├── config/          fail-closed release configuration
├── safety/          deployment policy
├── observability/   trace summaries
├── state.py
├── gates.py
├── orchestrator.py
├── system.py
└── run.py
```

### Agents
Build Agent, Registry Agent, Release Agent, Observability Agent, Incident and Rollback Agent, coordinated by the MLOps Orchestrator.

### Skills
Build validation, registry review, release planning, observability assessment, rollback readiness.

### Tools
Build fingerprint, registry record, release plan, monitoring plan, rollback plan.

See `docs/AGENTS_TOOLS_SKILLS.md`.

```bash
python -m src.run --example
pytest -q
```

The release gate fails closed when build, registry, change-control, observability, rollback, incident ownership, conflicts, or other material evidence is incomplete.

**Maturity: Reference implementation.** It does not autonomously deploy production models or alter infrastructure.

AI Engineering Handbook Series by Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H
