# octopus_core.py

from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Get the tokens and bot info
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
BOT_USERNAME = os.getenv("BOT_USERNAME")

def verify_tokens():
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("⚠️ Telegram Bot Token is missing or not set.")
    
    if not COHERE_API_KEY:
        raise ValueError("⚠️ Cohere API Key is missing or not set.")
    
    print("✅ Tokens loaded securely from .env!")
    print(f"🤖 Bot username: {BOT_USERNAME}")


if __name__ == "__main__":
    verify_tokens()
