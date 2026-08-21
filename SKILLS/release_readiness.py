from typing import Any, Dict, List

def release_readiness(case: Dict[str, Any]) -> Dict[str, Any]:
    required = ["build", "model", "release", "observability", "rollback"]
    missing: List[str] = [k for k in required if not case.get(k)]
    return {"missing": missing, "ready": not missing}
