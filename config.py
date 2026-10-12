# config.py
import os
from dotenv import load_dotenv

def get_api_key():
    load_dotenv()
    key = os.getenv("FAKE_API_KEY")
    if key is None or key.strip() == "":
        raise RuntimeError("FAKE_API_KEY 未配置或为空，请参考 .env.example")
    return key

