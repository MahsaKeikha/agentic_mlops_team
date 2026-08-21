# Architecture

`build evidence -> MLOps Orchestrator -> Build -> Registry -> Release -> Observability -> Incident/Rollback -> fail-closed release gate`

No specialist autonomously deploys infrastructure. The release gate remains blocked if build, registry, change-control, observability, rollback, or incident-ownership evidence is incomplete.
