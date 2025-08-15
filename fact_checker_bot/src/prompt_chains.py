import os
import yaml
from google import generativeai as genai
from src import utils
import os
from dotenv import load_dotenv

load_dotenv()
# Load API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=api_key)

class GeminiLLM:
    def __init__(self, model_name="gemini-2.5-flash"):
        self.model = genai.GenerativeModel(model_name)
        utils.log_info(f"Gemini LLM initialized with model: {model_name}")

    def predict(self, prompt: str) -> str:
        utils.log_debug(f"Sending prompt to Gemini:\n{prompt}")
        response = self.model.generate_content(contents=prompt)
        utils.log_debug("Received response from Gemini.")
        return response.text

class FactCheckChain:
    def __init__(self, llm=None, prompts_file="config/prompts.yaml"):
        self.llm = llm or GeminiLLM()
        with open(prompts_file, "r") as f:
            self.prompts = yaml.safe_load(f)
        utils.log_info("FactCheckChain initialized with prompts.")

    def initial_response(self, claim: str) -> str:
        template = self.prompts["initial_response"]["template"]
        prompt = template.format(claim=claim)
        return self.llm.predict(prompt)

    def extract_assumptions(self, initial_response: str) -> list:
        template = self.prompts["assumption_extraction"]["template"]
        prompt = template.format(initial_response=initial_response)
        assumptions_text = self.llm.predict(prompt)
        assumptions = [a.strip() for a in assumptions_text.split("\n") if a.strip()]
        utils.log_debug(f"Extracted assumptions: {assumptions}")
        return assumptions

    def final_synthesis(self, evidence_summary: str) -> str:
        template = self.prompts["final_synthesis"]["template"]
        prompt = template.format(evidence_summary=evidence_summary)
        return self.llm.predict(prompt)

























