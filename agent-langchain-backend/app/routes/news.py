from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/")
async def get_latest_news():
    news_api_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=your-newsapi-key"
    news_data = requests.get(news_api_url).json()
    headlines = [article["title"] for article in news_data.get("articles", [])]
    return {"news": headlines}
