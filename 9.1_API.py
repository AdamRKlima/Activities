import requests
import json
import pandas as pd 

# Send a GET request to the API
response = requests.get('https://jsonplaceholder.typicode.com/posts/')

# Parse the JSON response
data = json.loads(response.text)

df=pd.DataFrame(data)

print(df)