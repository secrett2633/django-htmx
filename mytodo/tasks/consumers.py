import json
import asyncio
import time

from channels.generic.http import AsyncHttpConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]

        # 클라이언트에게 메시지 전송
        await self.send(text_data=json.dumps({"message": f"서버 응답: {message}"}))


class SSEConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        await self.send_headers(headers=[
            (b"Cache-Control", b"no-cache"),
            (b"Content-Type", b"text/event-stream"),
            (b"Transfer-Encoding", b"chunked"),
        ])
        
        for i in range(10):
            data = f"현재 시간: {time.strftime('%H:%M:%S')}"
            await self.send_body(f"id: {i}\nevent: message\ndata: {data}\n\n".encode("utf-8"), more_body=True)
            await asyncio.sleep(1)
            
        await self.send_body(b"", more_body=False)
