from typing import Any, Dict

def incident_triage(incident: Dict[str, Any]) -> Dict[str, Any]:
    severity = str(incident.get("severity", "unknown")).lower()
    urgent = severity in {"critical", "sev0", "sev1", "high"}
    return {"severity": severity, "owner": incident.get("owner"), "urgent": urgent, "requires_human_incident_command": True}
