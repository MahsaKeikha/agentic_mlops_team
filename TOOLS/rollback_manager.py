from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class RollbackManager:
    def plan(self, current_version: str, target_version: str, reason: str) -> Dict[str, Any]:
        return {"current_version": current_version, "target_version": target_version, "reason": reason, "requires_approval": True, "tested": False}
