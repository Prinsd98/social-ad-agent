import json
from src.agents.creative_agent import CreativeAgent
from src.agents.copy_agent import CopyAgent
from src.agents.scheduler_agent import SchedulerAgent
from src.agents.analytics_agent import AnalyticsAgent

def run_campaign(config_path):
    with open(config_path) as f:
        spec = json.load(f)

    creative_agent = CreativeAgent()
    copy_agent = CopyAgent()
    scheduler = SchedulerAgent()
    analytics = AnalyticsAgent()

    creative = creative_agent.generate(spec)
    copy = copy_agent.write_copy(spec)
    schedule = scheduler.schedule(spec["platforms"])

    variants = [
        {"id": 1, "creative": creative, "copy": copy},
        {"id": 2, "creative": creative, "copy": copy}
    ]

    results, best = analytics.evaluate(variants)

    output = {
        "creative": creative,
        "copy": copy,
        "schedule": schedule,
        "results": results,
        "best_variant": best
    }

    print(json.dumps(output, indent=2))
    return output

if __name__ == "__main__":
    import sys
    run_campaign(sys.argv[1])
