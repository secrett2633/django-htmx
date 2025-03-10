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

        # GET 파라미터 받기
        if self.scope['method'] == 'GET':

            body_str = self.scope['query_string'].decode('utf-8')

        # POST 요청 본문 디코딩
        if self.scope['method'] == 'POST':
            # POST 요청 본문 디코딩

            body_str = body.decode('utf-8')
        print(body_str)
        
        # POST 요청 데이터 파싱 (application/x-www-form-urlencoded 형식 처리)
        # 'message=안녕하세요' 같은 형식이면 아래와 같이 파싱
        data = {}
        if body_str:
            params = body_str.split('&')
            for param in params:
                if '=' in param:
                    key, value = param.split('=', 1)
                    # URL 인코딩된 파라미터 디코딩
                    from urllib.parse import unquote_plus
                    data[key] = unquote_plus(value)
        
        user_message = data.get('message', '')
        print(user_message)
        
        for i, data in enumerate(user_message):
            await self.send_body(f"id: {i}\nevent: message\ndata: {data}\n\n".encode("utf-8"), more_body=True)
            await asyncio.sleep(1)
            
        await self.send_body(b"", more_body=False)
        