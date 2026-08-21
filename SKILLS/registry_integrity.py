from typing import Any, Dict

def registry_integrity(model: Dict[str, Any]) -> Dict[str, Any]:
    required = ["name", "version", "digest"]
    missing = [k for k in required if not model.get(k)]
    return {"missing": missing, "integrity_ok": not missing}
