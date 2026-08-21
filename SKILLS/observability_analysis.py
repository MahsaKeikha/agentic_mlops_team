from typing import Any, Dict

def observability_analysis(observability: Dict[str, Any]) -> Dict[str, Any]:
    alerts = bool(observability.get("alerts_configured")); drift = bool(observability.get("drift_monitoring")); slo = bool(observability.get("slo_defined"))
    return {"alerts_configured": alerts, "drift_monitoring": drift, "slo_defined": slo, "complete": alerts and drift and slo}
