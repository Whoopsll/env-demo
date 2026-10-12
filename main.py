from config import get_api_key

def mask_key(key):
    if len(key) <= 4:
        return "*****"
    SSKey = key[0:4]
    return f"{SSKey}*****"

try:
    key = get_api_key()
    print(mask_key(key))
except RuntimeError:
    print("请先配置 FAKE_API_KEY,参考 .env.example")


