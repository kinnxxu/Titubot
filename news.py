import requests
from config import NEWS_API_KEY

def get_latest_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=1&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url).json()
        article = response["articles"][0]
        return f"{article['title']}\n{article['url']}"
    except Exception as e:
        print("Error fetching news:", e)
        return None
