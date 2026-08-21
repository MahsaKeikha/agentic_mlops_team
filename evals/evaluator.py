def evaluate_result(r):
 a=r.get("analyses",{});return {"build_ready":"build" in a,"registry_ready":"registry" in a,"observability_ready":"observability" in a,"rollback_ready":"incident_rollback" in a,"blocked":r.get("status")=="blocked","trace_steps":len(r.get("trace",[]))}
