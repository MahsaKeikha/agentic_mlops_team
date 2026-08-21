from typing import Any, Dict

def rollback_planning(case: Dict[str, Any]) -> Dict[str, Any]:
    rollback = case.get("rollback", {})
    return {"target_version": rollback.get("target_version"), "tested": bool(rollback.get("tested")), "owner": rollback.get("owner"), "ready": bool(rollback.get("target_version") and rollback.get("tested") and rollback.get("owner"))}
