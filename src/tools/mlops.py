def build_fingerprint(c):return {"artifact":c.get("artifact"),"build_id":c.get("build_id"),"tests":c.get("tests")}
def registry_record(c):return {"model_version":c.get("model_version"),"registry_status":c.get("registry_status")}
def release_plan(c):return {"environment":c.get("environment"),"release_strategy":c.get("release_strategy"),"change_ticket":c.get("change_ticket")}
def monitoring_plan(c):return {"metrics":c.get("monitoring_metrics",[]),"alerts":c.get("alerts",[])}
def rollback_plan(c):return {"rollback":c.get("rollback"),"incident_owner":c.get("incident_owner")}
TOOL_MANIFEST=[{"name":n,"side_effects":False} for n in ("build_fingerprint","registry_record","release_plan","monitoring_plan","rollback_plan")]
