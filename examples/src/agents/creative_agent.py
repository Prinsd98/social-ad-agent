from src.tools.llm_tool import LLMTool

class CreativeAgent:
    def __init__(self):
        self.llm = LLMTool()

    def generate(self, spec):
        prompt = (
            f"Create an ad concept for {spec['product']} by {spec['brand']} "
            f"in a {spec['baseline_style']} style."
        )
        return {"prompt": prompt, "output": self.llm.generate(prompt)}
