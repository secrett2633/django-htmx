import asyncio
import ollama

from channels.generic.http import AsyncHttpConsumer


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
    
        stream = ollama.chat(
            model='deepseek-r1:32b',
            messages=[{'role': 'user', 'content': user_message}],
            stream=True,
        )

        for chunk in stream:
            data = chunk['message']['content']
            data = data.replace(" ", "&nbsp;")
            data = data.replace("\n", "<br/>")

            await self.send_body(f"event: message\ndata: {data}\n\n".encode("utf-8"), more_body=True)
            await asyncio.sleep(0)
            
        chat_id = self.scope['url_route']['kwargs']['chat_id']
        await self.send_body(f'event: message\ndata: <div id="chat-sse-listener-{chat_id}" hx-swap-oob="true"></div>\n\n'.encode("utf-8"), more_body=False)