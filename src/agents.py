"""Specialist agents for F32 Agentic MLOps Team."""
class BaseAgent:
    name="agent"; responsibility=""
    def run(self,state): raise NotImplementedError

class BuildAgent(BaseAgent):
    name="build"; responsibility="Validate build artifact, build identity, test evidence, and supply-chain metadata."
    def run(self,s):
        x={"artifact":s.case.get("artifact"),"build_id":s.case.get("build_id"),"tests":s.case.get("tests"),"sbom":s.case.get("sbom")};s.analyses[self.name]=x
        if not all([x["artifact"],x["build_id"],x["tests"]]): s.unresolved_questions.append("Build artifact, build ID, and test evidence are required")
        s.record(self.name,"validated build package",x)

class RegistryAgent(BaseAgent):
    name="registry"; responsibility="Review model version, registry state, lineage, and promotion metadata."
    def run(self,s):
        x={"model_version":s.case.get("model_version"),"registry_status":s.case.get("registry_status"),"lineage":s.case.get("lineage")};s.analyses[self.name]=x
        if not x["model_version"] or not x["registry_status"]: s.unresolved_questions.append("Model registry/version evidence is incomplete")
        s.record(self.name,"reviewed registry state",x)

class ReleaseAgent(BaseAgent):
    name="release"; responsibility="Prepare environment-specific rollout strategy, change control, and release gates."
    def run(self,s):
        x={"environment":s.case.get("environment"),"release_strategy":s.case.get("release_strategy"),"change_ticket":s.case.get("change_ticket"),"approval_policy":s.case.get("approval_policy")};s.analyses[self.name]=x
        if not all([x["environment"],x["release_strategy"],x["change_ticket"]]): s.risks.append("Release-control evidence is incomplete")
        s.record(self.name,"prepared release plan",x)

class ObservabilityAgent(BaseAgent):
    name="observability"; responsibility="Review service, model, data, drift, alerting, and SLO observability."
    def run(self,s):
        x={"metrics":s.case.get("monitoring_metrics",[]),"alerts":s.case.get("alerts",[]),"slos":s.case.get("slos",[])};s.analyses[self.name]=x
        if not x["metrics"]: s.risks.append("No production monitoring metrics supplied")
        s.record(self.name,"reviewed observability plan",x)

class IncidentRollbackAgent(BaseAgent):
    name="incident_rollback"; responsibility="Review rollback path, incident owner, recovery objective, and escalation plan."
    def run(self,s):
        x={"rollback":s.case.get("rollback"),"incident_owner":s.case.get("incident_owner"),"recovery_objective":s.case.get("recovery_objective"),"escalation":s.case.get("escalation")};s.analyses[self.name]=x
        if not x["rollback"] or not x["incident_owner"]: s.risks.append("Rollback or incident ownership is incomplete")
        s.record(self.name,"reviewed incident and rollback readiness",x)

def build_agents(): return [BuildAgent(),RegistryAgent(),ReleaseAgent(),ObservabilityAgent(),IncidentRollbackAgent()]
AGENT_MANIFEST=[{"name":c.name,"responsibility":c.responsibility} for c in [BuildAgent,RegistryAgent,ReleaseAgent,ObservabilityAgent,IncidentRollbackAgent]]
