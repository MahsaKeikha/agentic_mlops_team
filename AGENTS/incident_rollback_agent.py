from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class IncidentRollbackAgent:
    name: str = "incident_rollback_agent"
    responsibility: str = "Prepare incident ownership, containment, rollback criteria, and recovery evidence."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        incident = case.get("incident", {})
        rollback = case.get("rollback", {})
        return {"agent": self.name, "incident_owner": incident.get("owner"), "severity": incident.get("severity"), "rollback_target": rollback.get("target_version"), "rollback_tested": bool(rollback.get("tested")), "ready": bool(incident.get("owner") and rollback.get("target_version") and rollback.get("tested"))}
