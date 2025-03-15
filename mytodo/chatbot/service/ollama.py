import asyncio
import ollama

from shared.singleton import Singleton


class OllamaStreamService(Singleton):
    def __init__(self):
        pass
    
    async def get_stream(self, model: str, messages: list):
        return ollama.chat(
            model=model,
            messages=messages,
            stream=True,
        )
    
    async def process_stream(self, stream: ollama, send_body_func, chat_id: str = None):
        for chunk in stream:
            data: str = chunk["message"]["content"]
            data = data.replace(" ", "&nbsp;")
            data = data.replace("\n", "<br/>")

            await send_body_func(
                f"event: message\ndata: {data}\n\n".encode("utf-8"), 
                more_body=True
            )
            await asyncio.sleep(0)
        
        if chat_id:
            await send_body_func(
                f'event: message\ndata: <div id="chat-sse-listener-{chat_id}" hx-swap-oob="true"></div>\n\n'.encode("utf-8"),
                more_body=False,
            )

ollama_stream_service = OllamaStreamService()
