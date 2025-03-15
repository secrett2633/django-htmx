from django.http import HttpRequest
from django.shortcuts import render

from tasks.models import Task
from shared.views import get_navigation


class ChatbotService:
    @staticmethod
    def render_chatbot(request: HttpRequest):
        tasks: Task | None = Task.objects.all()
        return render(
            request, "chatbot.html", {"tasks": tasks, "navigation": get_navigation()}
        )

    @staticmethod
    def chat_send(request: HttpRequest, message: str):
        chat_id: int = request.session.get("chat_id", 1) + 1
        request.session["chat_id"] = chat_id
        context: dict[str, str | int] = {"human_message": message, "chat_id": chat_id}
        print(context)
        return render(request, "add_message.html", context)


chatbot_service = ChatbotService()
