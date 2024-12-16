import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

if not OPENAI_API_KEY:
    raise ValueError(
        "The OPENAI_API_KEY variable was not found in the .env file."
    )

if not ELEVENLABS_API_KEY:
    raise ValueError(
        "The ELEVENLABS_API_KEY variable was not found in the .env file."
    )
