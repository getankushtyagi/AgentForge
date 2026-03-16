import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from services.llm_service import LLMService
from schemas.product_schema import ProductSpecification


def clean_llm_json(text: str) -> str:
    """
    Clean Gemini responses that include markdown blocks.
    """
    text = text.strip()

    if text.startswith("```"):
        parts = text.split("```")

        if len(parts) > 1:
            text = parts[1]

            if text.startswith("json"):
                text = text[4:]

    return text.strip()


def main():

    llm = LLMService().get_llm()

    prompt = """
    Generate a product specification for a SaaS CRM platform.

    Return ONLY valid JSON.

    Required fields:
    - product_name
    - description
    - target_users
    - core_features
    - success_metrics

    Example format:

    {
      "product_name": "Example",
      "description": "Example description",
      "target_users": ["User1", "User2"],
      "core_features": ["Feature1", "Feature2"],
      "success_metrics": ["Metric1", "Metric2"]
    }
    """

    response = llm.invoke(prompt)

    if not response.content:
        raise ValueError("Empty response from Gemini")

    cleaned = clean_llm_json(response.content)

    data = json.loads(cleaned)

    product = ProductSpecification(**data)

    print("\nValidated Product Specification:\n")
    print(product.model_dump_json(indent=2))


if __name__ == "__main__":
    main()