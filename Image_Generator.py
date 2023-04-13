import os
import json
import openai
import requests
import random

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = f"WaterAlgae_{random.randint(0,10000)}.png"
        file_path = os.path.join(r"C:\Users\Sahil Sahu\Desktop\Smart Water Quality", file_name)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Image saved to {file_path}")
    else:
        print("Failed to download image")



os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
Response=openai.Image.create_variation(
  image=open("ALGAE3.png", "rb"),
  n=1,
  size="256x256"
)
json_string = json.dumps(Response)
response_dict = json.loads(json_string)
for obj in response_dict["data"]:
  download_image(obj["url"])