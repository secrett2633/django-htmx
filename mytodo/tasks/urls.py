from django.http import HttpRequest
from ninja import Router, Form

from tasks.service.render import render_service
from shared.reponse import BaseModel


router = Router(tags=[""])


@router.get(
    "",
    response={
        200: BaseModel,
    },
)
def index_handler(request: HttpRequest):
    return render_service.render_index_page(request)


@router.post(
    "/add/",
    response={
        200: BaseModel,
    },
)
def add_task_handler(request: HttpRequest, title: Form[str] = ""):
    return render_service.add_task(request, title)


@router.post(
    "toggle/{task_id}/",
    response={
        200: BaseModel,
    },
)
def toggle_task_handler(request: HttpRequest, task_id: int):
    return render_service.toggle_task(request, task_id)


@router.post(
    "delete/{task_id}/",
    response={
        200: BaseModel,
    },
)
def delete_task_handler(request: HttpRequest, task_id: int):
    return render_service.delete_task(request, task_id)


@router.get(
    "mobile_menu/",
    response={
        200: BaseModel,
    },
)
def mobile_menu_handler(request: HttpRequest):
    return render_service.mobile_menu(request)
