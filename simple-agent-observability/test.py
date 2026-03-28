import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

key = os.getenv("ANTHROPIC_API_KEY")
print(key)
print("prefix:", repr((key or "")[:12]))
client = Anthropic(api_key=key)

msg = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=20,
    messages=[{"role": "user", "content": "Say hello"}],
)

print(msg)
