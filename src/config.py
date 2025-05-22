import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Uniswap
UNISWAP_API_KEY = os.getenv("UNISWAP_API_KEY")
