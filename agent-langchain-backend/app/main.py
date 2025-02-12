from fastapi import FastAPI
from app.routes import chat, news  # ✅ Import API routes

app = FastAPI()

# ✅ Include API routes
app.include_router(chat.router, prefix="/chat")
app.include_router(news.router, prefix="/news")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)
