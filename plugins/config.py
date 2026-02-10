import os
from dotenv import load_dotenv

load_dotenv()

# BOT
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
TOKEN = os.environ.get("TOKEN")