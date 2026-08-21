from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass
class ModelRegistry:
    records: List[Dict[str, Any]] = field(default_factory=list)

    def register(self, name: str, version: str, digest: str, metadata: Dict[str, Any] | None = None) -> Dict[str, Any]:
        record = {"name": name, "version": version, "digest": digest, "metadata": metadata or {}}
        self.records.append(record)
        return record
