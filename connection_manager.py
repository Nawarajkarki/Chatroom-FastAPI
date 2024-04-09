from fastapi import WebSocket



class ConnectionManager:
    def __init__(self):
        # self.active_connections: list[WebSocket] = []
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self,chatroom:str, websocket: WebSocket):
        await websocket.accept()
        if chatroom not in self.active_connections:
            self.active_connections[chatroom] = []
            
        self.active_connections[chatroom].append(websocket)

    async def disconnect(self, chatroom:str, websocket: WebSocket):
        self.active_connections[chatroom].remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def broadcast(self, message: str, chatroom:str, sender: WebSocket = None):
        print(f"Active connections are {self.active_connections}")
        for connection in self.active_connections[chatroom]:
            if connection != sender:
                await connection.send_text(message)
                