import os, json, time
from dotenv import load_dotenv
from mem0 import MemoryClient

load_dotenv()
client = MemoryClient(api_key=os.getenv("MEM0_API_KEY"))

USER = "demo_user"

# print("ADD")
# print(json.dumps(
#     client.add(
#         messages=[{"role": "user", "content": "I like scikit-learn"}],
#         user_id=USER
#     ),
#     indent=2
# ))

time.sleep(5)

print("\nGET_ALL user only")
print(json.dumps(client.get_all(filters={"user_id": USER}, version="v2"), indent=2))

print("\nSEARCH user only")
print(json.dumps(client.search("scikit-learn", filters={"user_id": USER}, version="v2"), indent=2))