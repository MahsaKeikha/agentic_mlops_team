from dataclasses import dataclass,field
from typing import Any,Dict,List
from uuid import uuid4
from .agents import build_agents
SYSTEM_ID,SYSTEM_NAME,VERSION="F32","Agentic MLOps Team","0.2.0"
@dataclass
class State:
    case:Dict[str,Any];run_id:str=field(default_factory=lambda:str(uuid4()));analyses:Dict[str,Any]=field(default_factory=dict);evidence:List[Dict[str,str]]=field(default_factory=list);unresolved_questions:List[str]=field(default_factory=list);conflicts:List[str]=field(default_factory=list);risks:List[str]=field(default_factory=list);trace:List[Dict[str,Any]]=field(default_factory=list)
    def record(self,a,e,x=None): self.trace.append({"step":len(self.trace)+1,"actor":a,"event":e,"artifact":x})
def run_system(case:Dict[str,Any],approve=False):
    s=State(case);s.record("mlops_orchestrator","run started",{"system_id":SYSTEM_ID,"version":VERSION})
    for a in build_agents(): a.run(s)
    for e in case.get("evidence",[]): s.evidence.append({"claim":str(e.get("claim","")),"source":str(e.get("source","")),"status":str(e.get("status","supplied"))})
    s.conflicts.extend(case.get("conflicts",[]))
    blockers=bool(s.unresolved_questions or s.conflicts or s.risks)
    status="approved_for_human_follow_through" if approve and not blockers else "blocked" if blockers else "awaiting_human_approval"
    s.record("mlops_orchestrator","release gate evaluated",{"approve":approve,"blockers":blockers,"status":status})
    return {"system_id":SYSTEM_ID,"system_name":SYSTEM_NAME,"version":VERSION,"run_id":s.run_id,"domain":"mlops","analyses":s.analyses,"evidence":s.evidence,"unresolved_questions":s.unresolved_questions,"conflicts":s.conflicts,"risks":s.risks,"recommendation":"Resolve release blockers." if blockers else "Release package is ready for authorized human review.","status":status,"trace":s.trace}
