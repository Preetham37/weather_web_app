import requests
import os
from dotenv import load_dotenv

load_dotenv()

data_from_api=requests.get(os.getenv("WEB_URL_API"))

print(data_from_api.json())
