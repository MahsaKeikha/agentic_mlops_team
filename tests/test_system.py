from src.system import run_system
def case():return {"artifact":"a","build_id":"b","tests":"pass","model_version":"1","registry_status":"registered","environment":"staging","release_strategy":"canary","change_ticket":"c","monitoring_metrics":["latency"],"alerts":["alert"],"rollback":"prior","incident_owner":"team"}
def test_waits_for_human():assert run_system(case())["status"]=="awaiting_human_approval"
def test_clean_approval():assert run_system(case(),True)["status"]=="approved_for_human_follow_through"
def test_no_rollback_blocks():
 c=case();c["rollback"]=None;assert run_system(c,True)["status"]=="blocked"
def test_missing_tests_blocks():
 c=case();c["tests"]=None;assert run_system(c,True)["status"]=="blocked"
