import json

from services.llm_service import LLMService
from schemas.backend_schema import BackendDesign


class BackendEngineerAgent:

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

    def generate_backend_design(self, architecture: dict):

        prompt = f"""
        You are a senior backend engineer.

        Based on the following system architecture, design the backend.

        Architecture:
        {architecture}

        Return ONLY valid JSON with this format:

        {{
          "api_endpoints": ["string1", "string2"],
          "database_models": ["string1", "string2"],
          "backend_services": ["string1", "string2"]
        }}

        IMPORTANT:
        - api_endpoints must be REST endpoints
        - database_models must be entity names
        - backend_services must be service names
        """

        response = self.llm.invoke(prompt)

        cleaned = self.clean_llm_json(response.content)

        data = json.loads(cleaned)

        return BackendDesign(**data)