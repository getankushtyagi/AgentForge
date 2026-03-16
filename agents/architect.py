import json

from services.llm_service import LLMService
from schemas.architecture_schema import SystemArchitecture


class ArchitectAgent:

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

    def generate_architecture(self, product_spec: dict):

        prompt = f"""
        You are a senior software architect.

        Based on the following product specification, design a system architecture.

        Product Specification:
        {product_spec}

        Return ONLY valid JSON matching this EXACT format:
        {{
          "services": ["string1", "string2"],
          "database_table": ["string1", "string2"],
          "tech_stack": ["string1", "string2"]
        }}

        IMPORTANT: 
        - All fields must be arrays of STRINGS only
        - Do NOT use objects or nested structures
        - Return ONLY the JSON, no markdown, no explanations
        """

        response = self.llm.invoke(prompt)

        cleaned = self.clean_llm_json(response.content)

        data = json.loads(cleaned)

        return SystemArchitecture(**data)