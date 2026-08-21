from typing import Any
from .base import BaseAgent
from ..skills import validate_build, review_registry, plan_release, assess_observability, assess_rollback_readiness
from ..tools import build_fingerprint, registry_record, release_plan, monitoring_plan, rollback_plan
class BuildAgent(BaseAgent):
 name="build";responsibility="Validate build artifact and CI evidence.";required_skills=("validate_build",);allowed_tools=("build_fingerprint",)
 def run(self,s:Any):
  a=validate_build(build_fingerprint(s.case));s.analyses[self.name]=a;s.unresolved_questions.extend(a["questions"]);s.record(self.name,"validated build",a)
class RegistryAgent(BaseAgent):
 name="registry";responsibility="Verify model registry and version state.";required_skills=("review_registry",);allowed_tools=("registry_record",)
 def run(self,s:Any):
  a=review_registry(registry_record(s.case));s.analyses[self.name]=a;s.unresolved_questions.extend(a["questions"]);s.record(self.name,"reviewed registry",a)
class ReleaseAgent(BaseAgent):
 name="release";responsibility="Prepare controlled release and change plan.";required_skills=("plan_release",);allowed_tools=("release_plan",)
 def run(self,s:Any):
  a=plan_release(release_plan(s.case));s.analyses[self.name]=a;s.risks.extend(a["risks"]);s.record(self.name,"planned release",a)
class ObservabilityAgent(BaseAgent):
 name="observability";responsibility="Assess metrics, alerts and runtime visibility.";required_skills=("assess_observability",);allowed_tools=("monitoring_plan",)
 def run(self,s:Any):
  a=assess_observability(monitoring_plan(s.case));s.analyses[self.name]=a;s.risks.extend(a["risks"]);s.record(self.name,"assessed observability",a)
class IncidentRollbackAgent(BaseAgent):
 name="incident_rollback";responsibility="Assess incident ownership and rollback readiness.";required_skills=("assess_rollback_readiness",);allowed_tools=("rollback_plan",)
 def run(self,s:Any):
  a=assess_rollback_readiness(rollback_plan(s.case));s.analyses[self.name]=a;s.risks.extend(a["risks"]);s.record(self.name,"assessed rollback readiness",a)
CLASSES=[BuildAgent,RegistryAgent,ReleaseAgent,ObservabilityAgent,IncidentRollbackAgent]
def build_agents():return [c() for c in CLASSES]
AGENT_MANIFEST=[{"name":c.name,"responsibility":c.responsibility,"skills":list(c.required_skills),"tools":list(c.allowed_tools)} for c in CLASSES]
