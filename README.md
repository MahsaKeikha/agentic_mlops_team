# F32 Agentic MLOps Team

Standalone multi-agent reference architecture for controlled model delivery, release governance, observability, incident response, and rollback planning.

## Repository map

```text
.github/workflows/tests.yml
src/agents.py
src/state.py
src/gates.py
src/orchestrator.py
src/system.py
src/run.py
evals/evaluator.py
examples/release_case.json
benchmarks/README.md
docs/ARCHITECTURE.md
tests/
SECURITY.md
CONTRIBUTING.md
CITATION.cff
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
pyproject.toml
```

## Multi-agent team
Build Agent, Registry Agent, Release Agent, Observability Agent, Incident and Rollback Agent, and MLOps Orchestrator.

The release gate fails closed when build, registry, change-control, observability, rollback, incident ownership, conflicts, or other material evidence is incomplete.

```bash
python -m src.run --example
pytest -q
```

**Maturity: Reference implementation.** It does not autonomously deploy production models or alter infrastructure.

AI Engineering Handbook Series by Mahsa Keikha:
- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H
