import asyncio
import ollama

from channels.generic.http import AsyncHttpConsumer


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

        stream: ollama.StreamResponse = ollama.chat(
            model="deepseek-r1:32b",
            messages=[{"role": "user", "content": user_message}],
            stream=True,
        )

        for chunk in stream:
            data: str = chunk["message"]["content"]
            data: str = data.replace(" ", "&nbsp;")
            data: str = data.replace("\n", "<br/>")

            await self.send_body(
                f"event: message\ndata: {data}\n\n".encode("utf-8"), more_body=True
            )
            await asyncio.sleep(0)

        chat_id: str = self.scope["url_route"]["kwargs"]["chat_id"]
        await self.send_body(
            f'event: message\ndata: <div id="chat-sse-listener-{chat_id}" hx-swap-oob="true"></div>\n\n'.encode(
                "utf-8"
            ),
            more_body=False,
        )
