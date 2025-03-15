from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from tasks.models import Task


class RenderService:
    @staticmethod
    def get_navigation():
        return [
            {"name": "챗봇", "href": "/chatbot"},
            {"name": "코인", "href": "/coin"},
        ]

    @staticmethod
    def render_index_page(request: HttpRequest):
        tasks: Task = Task.objects.all()
        return render(
            request,
            "shared/index.html",
            {"tasks": tasks, "navigation": render_service.get_navigation()},
        )

    @staticmethod
    def add_task(request: HttpRequest, title: str = ""):
        if title:
            task: Task = Task.objects.create(title=title)
            return render(request, "shared/task_item.html", {"task": task})
        return HttpResponse(status=400)

    @staticmethod
    def toggle_task(request: HttpRequest, task_id: int):
        task: Task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()
        return render(request, "shared/task_item.html", {"task": task})

    @staticmethod
    def delete_task(request: HttpRequest, task_id: int):
        task: Task = get_object_or_404(Task, id=task_id)
        task.delete()
        return HttpResponse("")

    @staticmethod
    def mobile_menu(request: HttpRequest):
        context: dict[str, Any] = {
            "navigation": render_service.get_navigation(),
            "user": request.user,
        }
        return render(request, "shared/mobile_menu.html", context)


render_service = RenderService()
