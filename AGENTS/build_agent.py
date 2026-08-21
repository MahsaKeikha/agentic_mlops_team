from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class BuildAgent:
    name: str = "build_agent"
    responsibility: str = "Validate build provenance, dependencies, tests, and immutable artifact identity."

    def run(self, case: Dict[str, Any]) -> Dict[str, Any]:
        build = case.get("build", {})
        return {"agent": self.name, "artifact": build.get("artifact"), "tests_passed": bool(build.get("tests_passed")), "provenance": build.get("provenance"), "ready": bool(build.get("artifact") and build.get("tests_passed") and build.get("provenance"))}
