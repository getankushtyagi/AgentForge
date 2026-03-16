from dotenv import load_dotenv
import os

load_dotenv()

# Fix gRPC DNS resolution issues on macOS
if os.getenv("GRPC_DNS_RESOLVER"):
    os.environ["GRPC_DNS_RESOLVER"] = os.getenv("GRPC_DNS_RESOLVER")

class Settings:
    GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
    
    
settings=Settings()