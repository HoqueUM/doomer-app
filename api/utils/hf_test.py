"""
Hugging face space accessing test.
"""
# print(response.json())

from huggingface_hub import HfApi
import dotenv
import os

dotenv.load_dotenv()
HF_TOKEN = os.environ.get("HF_TOKEN")


api = HfApi()



# api.pause_space(repo_id="rhoque/doomer", token=HF_TOKEN)
#api.restart_space(repo_id="rhoque/doomer", token=HF_TOKEN)

import requests

api.restart_space(repo_id="rhoque/doomer", token=HF_TOKEN)

payload = {
    "title": "Global temps rising, iceland is now a desert"
}

url = "https://rhoque-doomer.hf.space/sentiment"

response = requests.post(url, json=payload)
print(response.json())
print(response.status_code)