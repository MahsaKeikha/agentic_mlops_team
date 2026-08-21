from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class ObservabilityAgent:
    name: str = "observability_agent"
    responsibility: str = "Assess service health, drift, quality, latency, and alert coverage before and after release."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        obs = case.get("observability", {})
        return {"agent": self.name, "metrics": dict(obs.get("metrics", {})), "alerts_configured": bool(obs.get("alerts_configured")), "drift_monitoring": bool(obs.get("drift_monitoring")), "ready": bool(obs.get("alerts_configured") and obs.get("drift_monitoring"))}
