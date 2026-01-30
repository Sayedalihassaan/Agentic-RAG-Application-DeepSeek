import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Validate that required API keys are present
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found in environment variables. Please set it in your .env file.")

if not OPEN_ROUTER_API_KEY:
    raise ValueError("OPEN_ROUTER_API_KEY not found in environment variables. Please set it in your .env file.")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables. Please set it in your .env file.")