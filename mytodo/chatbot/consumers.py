from channels.generic.http import AsyncHttpConsumer

from chatbot.service.ollama import ollama_stream_service

class ChatConsumer(AsyncHttpConsumer):
    async def handle(self, body: bytes):
        await self.send_headers(
            headers=[
                (b"Cache-Control", b"no-cache"),
                (b"Content-Type", b"text/event-stream"),
                (b"Transfer-Encoding", b"chunked"),
                (b"Access-Control-Allow-Origin", b"*"),
                (b"Connection", b"keep-alive"),
            ]
        )

        user_message: str = self.scope["url_route"]["kwargs"]["message"]
        chat_id: str = self.scope["url_route"]["kwargs"]["chat_id"]

        stream = await ollama_stream_service.get_stream(
            model="deepseek-r1:32b",
            messages=[{"role": "user", "content": user_message}]
        )

        await ollama_stream_service.process_stream(
            stream=stream, 
            send_body_func=self.send_body, 
            chat_id=chat_id
        )
