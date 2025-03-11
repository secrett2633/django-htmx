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

class ChatConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        # SSE 헤더 설정
        await self.send_headers(headers=[
            (b"Cache-Control", b"no-cache"),
            (b"Content-Type", b"text/event-stream"),
            (b"Transfer-Encoding", b"chunked"),
            (b"Access-Control-Allow-Origin", b"*"),  # CORS 문제 해결
            (b"Connection", b"keep-alive"),  # 연결 유지
        ])        
        
        user_message = self.scope['url_route']['kwargs']['message']
        for i, data in enumerate("SSE 응답 테스트입니다. '" + user_message + "' 메세지에 대한 LLM 응답은 추후에 추가될 예정입니다."):
            if data == " ":
                data = "&nbsp;"
            await self.send_body(f"id: {i}\nevent: message\ndata: {data}\n\n".encode("utf-8"), more_body=True)
            await asyncio.sleep(0.05)        
        
        chat_id = self.scope['url_route']['kwargs']['chat_id']
        await self.send_body(f'event: message\ndata: <div id="chat-sse-listener-{chat_id}" hx-swap-oob="true"></div>\n\n'.encode("utf-8"), more_body=False)
