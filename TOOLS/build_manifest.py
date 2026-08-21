from dataclasses import dataclass
from hashlib import sha256
from typing import Any, Dict

@dataclass
class BuildManifest:
    def create(self, artifact: str, dependencies: Dict[str, str], commit: str) -> Dict[str, Any]:
        digest = sha256(f"{artifact}|{commit}|{sorted(dependencies.items())}".encode()).hexdigest()
        return {"artifact": artifact, "commit": commit, "dependencies": dict(dependencies), "digest": digest}
