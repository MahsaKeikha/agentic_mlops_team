def validate_build(a):
 q=[]
 if not all(a.values()):q.append("Build artifact, build ID, and test evidence are required")
 return {**a,"questions":q}
def review_registry(a):
 q=[]
 if not all(a.values()):q.append("Model registry/version evidence is incomplete")
 return {**a,"questions":q}
def plan_release(a):
 return {**a,"risks":([] if all(a.values()) else ["Release-control evidence is incomplete"])}
def assess_observability(a):
 return {**a,"risks":([] if a["metrics"] else ["No production monitoring metrics supplied"])}
def assess_rollback_readiness(a):
 return {**a,"risks":([] if all(a.values()) else ["Rollback or incident ownership is incomplete"])}
SKILL_MANIFEST=["validate_build","review_registry","plan_release","assess_observability","assess_rollback_readiness"]
