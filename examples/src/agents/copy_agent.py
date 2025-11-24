from src.tools.llm_tool import LLMTool

class CopyAgent:
    def __init__(self):
        self.llm = LLMTool()

    def write_copy(self, spec):
        headline = f"{spec['product']} – Glow Naturally"
        caption = f"Experience pure Ayurvedic radiance with {spec['product']}. Tap to order."
        cta = "Buy Now"
        return {"headline": headline, "caption": caption, "cta": cta}
