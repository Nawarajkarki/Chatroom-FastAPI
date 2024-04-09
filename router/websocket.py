from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from connection_manager import ConnectionManager

router = APIRouter()
    
manager = ConnectionManager()


@router.websocket("/ws/{chatroom}/{username}")
async def websocket_endpoint(websocket: WebSocket,chatroom:str, username: str):
    await manager.connect(chatroom=chatroom, websocket=websocket)
    await websocket.send_text("You joined the chat")
    await manager.broadcast(message= f"{username} joined the chat", chatroom=chatroom, sender= websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You: {data}", websocket)
            await manager.broadcast(
                message=f"{username}: {data}",
                chatroom=chatroom, 
                sender= websocket
            )
            
    except WebSocketDisconnect:
        # await manager.broadcast(message=f"{username} left the chat",chatroom=chatroom, sender= websocket)
        manager.disconnect(chatroom=chatroom, websocket=websocket)

