from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class RegistryAgent:
    name: str = "registry_agent"
    responsibility: str = "Verify model registry identity, version immutability, lineage, and stage metadata."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        model = case.get("model", {})
        return {"agent": self.name, "name": model.get("name"), "version": model.get("version"), "digest": model.get("digest"), "lineage": model.get("lineage"), "registered": bool(model.get("name") and model.get("version") and model.get("digest"))}
