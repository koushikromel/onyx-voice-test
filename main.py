from fastapi import FastAPI
from pydantic import BaseModel
import openai
import keys
app = FastAPI(title="Onyx Api", docs_url="/admin", redoc_url="/document")
openai.api_key = keys.key



@app.post("/")
async def Commands():
    reply = {'reply':'your message was recorded successfully'}
    return reply

