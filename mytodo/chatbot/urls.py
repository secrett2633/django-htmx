from django.http import HttpRequest
from ninja import Router, Form

from chatbot.service.chatbot import chatbot_service
from shared.reponse import BaseModel


router = Router(tags=[""])


@router.get("chatbot", response=BaseModel)
def chatbot_handler(request: HttpRequest):
    return chatbot_service.render_chatbot(request)


@router.post("/chat/send", response=BaseModel)
def chat_send_handler(request: HttpRequest, message: Form[str]):
    return chatbot_service.chat_send(request, message)
