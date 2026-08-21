from .agents import build_agents
from .gates import evaluate_release_gate
from .state import RunState
SYSTEM_ID,SYSTEM_NAME,VERSION="F32","Agentic MLOps Team","0.2.0"
def run_system(case,approve=False):
 s=RunState(case);s.record("mlops_orchestrator","run started",{"system_id":SYSTEM_ID,"version":VERSION})
 for a in build_agents():a.run(s)
 for e in case.get("evidence",[]):s.evidence.append({"claim":str(e.get("claim","")),"source":str(e.get("source","")),"status":str(e.get("status","supplied"))})
 s.conflicts.extend(case.get("conflicts",[]));status=evaluate_release_gate(s,approve);s.record("mlops_orchestrator","release gate evaluated",{"approve":approve,"status":status})
 return {"system_id":SYSTEM_ID,"system_name":SYSTEM_NAME,"version":VERSION,"run_id":s.run_id,"domain":"mlops","analyses":s.analyses,"evidence":s.evidence,"unresolved_questions":s.unresolved_questions,"conflicts":s.conflicts,"risks":s.risks,"recommendation":"Resolve release blockers." if status=="blocked" else "Release package is ready for authorized human review.","status":status,"trace":s.trace}
