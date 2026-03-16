import json
from services.llm_service import LLMService
from schemas.product_schema import ProductSpecification


class ProductManagerAgent:
    def __init__(self):
        self.llm=LLMService().get_llm()
        
    def clean_llm_json(self,text:str)->str:
        # clean the gemini resoponse that content markdown blocks
        text=text.strip()
        
        if text.startswith("```"):
            parts=text.split("```")
            
            if len(parts)>1:
                text=parts[1]
                
                if text.startswith("json"):
                    text=text[4:]
        return text.strip()
    
    def generate_product_spec(self, idea:str)->ProductSpecification:
        
        prompt = f"""
        You are a senior product manager.

        Convert the following product idea into a structured product specification.

        Idea:
        {idea}

        Return ONLY valid JSON matching this EXACT format:
        {{
          "product_name": "string - name of the product",
          "description": "string - detailed description",
          "target_users": ["string1", "string2", "string3"],
          "core_features": ["string1", "string2", "string3"],
          "success_metrics": ["string1", "string2", "string3"]
        }}

        IMPORTANT: 
        - target_users, core_features, and success_metrics must be arrays of STRINGS only
        - Do NOT use objects or nested structures
        - Each feature should be a simple descriptive string
        - Return ONLY the JSON, no markdown, no explanations
        """
        
        response=self.llm.invoke(prompt)
        
        if not response.content:
            raise ValueError("LLM return empty response")
        cleaned = self.clean_llm_json(response.content)
        
        data =json.loads(cleaned)
        
        product_spec=ProductSpecification(**data)
        
        return product_spec