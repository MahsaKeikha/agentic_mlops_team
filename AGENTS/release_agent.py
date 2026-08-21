from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class ReleaseAgent:
    name: str = "release_agent"
    responsibility: str = "Evaluate release evidence, change approval, rollout strategy, and release blockers."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        release = case.get("release", {})
        required = ["change_id", "approval_owner", "rollout_strategy"]
        missing: List[str] = [k for k in required if not release.get(k)]
        return {"agent": self.name, "missing": missing, "ready": not missing}
