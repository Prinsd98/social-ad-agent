class SchedulerAgent:
    def schedule(self, platforms):
        return [
            {"platform": p, "time": "Tomorrow 10:00 AM"}
            for p in platforms
        ]
