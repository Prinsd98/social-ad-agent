from src.utils.stats import fake_metrics
from src.memory.memory_bank import MemoryBank

class AnalyticsAgent:
    def __init__(self):
        self.memory = MemoryBank()

    def evaluate(self, variants):
        results = []
        for v in variants:
            metrics = fake_metrics(2000)
            v["metrics"] = metrics
            results.append(v)

        best = max(results, key=lambda x: x["metrics"]["conversions"])
        self.memory.store_win(best)
        return results, best
