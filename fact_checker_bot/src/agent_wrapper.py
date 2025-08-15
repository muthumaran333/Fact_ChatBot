import os
from typing import List, Optional
from pydantic import PrivateAttr
from langchain.llms.base import LLM
from src.prompt_chains import GeminiLLM
from src.search_tools import EvidenceSearch


# LLM Wrapper
class LangChainGemini(LLM):
    _gemini: GeminiLLM = PrivateAttr()

    def __init__(self):
        super().__init__()
        self._gemini = GeminiLLM()

    @property
    def _llm_type(self):
        return "gemini"

    def _call(self, prompt: str, stop: Optional[List[str]] = None):
        return self._gemini.predict(prompt)


# Evidence Tool Wrapper
class EvidenceTool:
    """Simple wrapper around EvidenceSearch."""
    def __init__(self, tavily_api_key: str):
        self._searcher = EvidenceSearch(tavily_api_key=tavily_api_key)

    def run(self, query: str):
        return self._searcher.gather_evidence([query])


# Custom Fact-Checking Pipeline
class FactChecker:
    def __init__(self, tavily_api_key: str):
        self.llm = LangChainGemini()
        self.tool = EvidenceTool(tavily_api_key)

    def check_claim(self, claim: str) -> str:
        # Extract assumptions
        assumptions_prompt = f"Extract assumptions from the claim: {claim}"
        assumptions_text = self.llm._call(assumptions_prompt)
        assumptions = [a.strip() for a in assumptions_text.split("\n") if a.strip()]

        # Gather evidence
        evidence_summary = []
        for a in assumptions:
            evidence = self.tool.run(a)
            evidence_summary.append(f"Assumption: {a}\nEvidence: {evidence}\n")

        # Final synthesis
        synthesis_prompt = (
            f"Claim: {claim}\n"
            f"Evidence Summary:\n{''.join(evidence_summary)}\n"
            f"Provide a single final verdict (True/False) and a concise explanation."
        )
        final_answer = self.llm._call(synthesis_prompt)
        return final_answer


# Factory function for Streamlit
def get_agent():
    return FactChecker(tavily_api_key=os.getenv("TAVILY_API_KEY"))








