from dataclasses import dataclass
from typing import Dict, Iterable

@dataclass
class TelemetryReader:
    def summarize(self, values: Iterable[float]) -> Dict[str, float]:
        data = list(values)
        if not data:
            return {"count": 0, "min": 0.0, "max": 0.0, "mean": 0.0}
        return {"count": len(data), "min": min(data), "max": max(data), "mean": sum(data) / len(data)}
