import json

from services.llm_service import LLMService
from schemas.qa_schema import QAPlan


class QAEngineerAgent:

    def __init__(self):
        self.llm = LLMService().get_llm()

    def clean_llm_json(self, text: str):

        text = text.strip()

        if text.startswith("```"):
            parts = text.split("```")

            if len(parts) > 1:
                text = parts[1]

                if text.startswith("json"):
                    text = text[4:]

        return text.strip()

    def generate_test_plan(self, backend_design: dict):

        prompt = f"""
        You are a senior QA engineer.

        Based on the backend system design below, generate a testing plan.

        Backend Design:
        {backend_design}

        Return ONLY valid JSON matching this EXACT format:
        {{
          "test_cases": ["string1", "string2"],
          "edge_cases": ["string1", "string2"],
          "api_test": ["string1", "string2"]
        }}

        IMPORTANT: 
        - All fields must be arrays of STRINGS only
        - Do NOT use objects or nested structures
        - Return ONLY the JSON, no markdown, no explanations
        """

        response = self.llm.invoke(prompt)

        cleaned = self.clean_llm_json(response.content)

        data = json.loads(cleaned)

        return QAPlan(**data)