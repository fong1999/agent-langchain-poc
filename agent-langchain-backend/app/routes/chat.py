from fastapi import APIRouter
from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel

router = APIRouter()
llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

class ChatRequest(BaseModel):
    message: str

@router.post("/")
async def chat(request: ChatRequest):
    response = llm.predict(request.message)
    return {"response": response}
