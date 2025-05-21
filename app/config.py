import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", 8000))
AI_API_KEY = os.getenv("AI_API_KEY", "")
