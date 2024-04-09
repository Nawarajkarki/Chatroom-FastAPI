from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from router.websocket import router


app = FastAPI()
app.include_router(router)


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name='static')


# @app.get("/", response_class=HTMLResponse)
# async def get(chatroom: str = "chat"):
#     return templates.TemplateResponse("chatroom.html", {"request": {}, "chatroom": "Chat App"})

@app.get("/{chatroom}", response_class=HTMLResponse)
async def get(chatroom: str = "chat"):
    return templates.TemplateResponse("chatroom.html", {"request": {}, "chatroom": chatroom})

