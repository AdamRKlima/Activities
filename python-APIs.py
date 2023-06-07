import requests
from dotenv import load_dotenv 
import pandas as pd 
import json 
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv('API_KEY')

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(dir(response))
print(api_key)