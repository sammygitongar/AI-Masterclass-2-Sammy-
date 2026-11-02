
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

country = "us" 

url = f"https://newsapi.org/v2/top-headlines?country={country}&pageSize=5&apiKey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    articles = data['articles']

    print("Top 5 news headlines in the US:")

    for index, article in enumerate(articles, start=1):
        title = article['title']
        description = article['description']
        url = article['url']

        print(f"{index}. {title}")
        print(f"Description: {description}")
        #print(f"URL: {url}")
        print("-" * 80)
elif response.status_code == 401:
    print("Error: Unauthorized. Please check your API key.")
elif response.status_code == 404:
    print("Error: Resource not found. Check the URL or parameters.")
else:
    print("Error:", response.status_code)
    print(response.text)
