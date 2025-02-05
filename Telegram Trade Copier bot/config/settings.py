import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TROJAN_API_KEY = os.getenv("TROJAN_API_KEY")
BULLX_API_KEY = os.getenv("BULLX_API_KEY")