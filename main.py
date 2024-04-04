from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from router.websocket import router


app = FastAPI()
app.include_router(router)


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get():
    return templates.TemplateResponse("chat3.html", {"request": {}})


