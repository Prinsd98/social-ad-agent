import random

def fake_metrics(impressions: int):
    ctr = round(random.uniform(0.8, 4.5), 2)
    clicks = int(impressions * ctr / 100)
    conversions = int(clicks * random.uniform(0.05, 0.25))
    return {
        "impressions": impressions,
        "ctr": ctr,
        "clicks": clicks,
        "conversions": conversions
    }
