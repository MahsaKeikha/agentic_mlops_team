import argparse,json
from .system import run_system
EXAMPLE={"artifact":"model.tar.gz","build_id":"build-101","tests":"passed fixture","model_version":"1.2.0","registry_status":"registered","environment":"staging","release_strategy":"canary","change_ticket":"CHG-101","monitoring_metrics":["latency","error_rate","model_quality"],"alerts":["error budget"],"rollback":"restore 1.1.0","incident_owner":"ml platform on-call","evidence":[{"claim":"tests passed","source":"CI fixture","status":"supplied"}]}
def main():
 p=argparse.ArgumentParser();p.add_argument("--example",action="store_true");p.add_argument("--approve",action="store_true");a=p.parse_args();print(json.dumps(run_system(EXAMPLE if a.example else {},a.approve),indent=2))
if __name__=="__main__":main()
