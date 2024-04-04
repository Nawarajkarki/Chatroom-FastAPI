from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from connection_manager import ConnectionManager

router = APIRouter()
    
manager = ConnectionManager()


@router.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    await websocket.send_text("You joined the chat")
    await manager.broadcast(f"{username} joined the chat", websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You: {data}", websocket)
            await manager.broadcast(f"{username}: {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

        await manager.broadcast(f"User {username} left the chat")
