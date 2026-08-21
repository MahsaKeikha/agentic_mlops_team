from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class DeploymentPlan:
    def create(self, version: str, strategy: str = "canary", percentage: int = 10) -> Dict[str, Any]:
        return {"version": version, "strategy": strategy, "initial_percentage": max(1, min(100, int(percentage))), "human_approval_required": True}
