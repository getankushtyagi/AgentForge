from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import settings


class LLMService:

    def __init__(self):

        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0.2,
            response_mime_type="application/json"
        )

    def get_llm(self):
        return self.model