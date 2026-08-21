from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"AGENTS": ["build_agent.py", "registry_agent.py", "release_agent.py", "observability_agent.py", "incident_rollback_agent.py"], "TOOLS": ["build_manifest.py", "model_registry.py", "deployment_plan.py", "telemetry_reader.py", "rollback_manager.py"], "SKILLS": ["release_readiness.py", "registry_integrity.py", "observability_analysis.py", "incident_triage.py", "rollback_planning.py"]}
def test_visible_components_exist_and_compile():
    for folder, names in EXPECTED.items():
        for name in names:
            path = ROOT / folder / name
            assert path.exists(), path
            compile(path.read_text(), str(path), "exec")
