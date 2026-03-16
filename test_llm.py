import os
from dotenv import load_dotenv
from services.llm_service import LLMService

# Load environment variables
load_dotenv()

# Set GRPC DNS resolver before any gRPC imports
os.environ["GRPC_DNS_RESOLVER"] = "native"

llm=LLMService().get_llm()
response = llm.invoke("explain microservice architecture in simple words")
print(response.content)