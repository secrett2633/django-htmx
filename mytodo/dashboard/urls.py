from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from ninja import Router

from dashboard.service.render import render_service
from shared.reponse import BaseModel


router = Router(tags=[""])


@login_required
@router.get(
    "dashboard/",
    response={
        200: BaseModel,
    },
)
def dashboard_handler(request: HttpRequest):
    return render_service.render_dashboard_page(request)


@login_required
@router.get(
    "edit_name/",
    response={
        200: BaseModel,
    },
)
@router.post(
    "edit_name/",
    response={
        200: BaseModel,
    },
)
def edit_name_handler(request: HttpRequest):
    if request.method == "GET":
        return render_service.render_edit_name_page(request)
    if request.method == "POST":
        return render_service.edit_name(request)


@login_required
@router.get(
    "edit_phone/",
    response={
        200: BaseModel,
    },
)
@router.post(
    "edit_phone/",
    response={
        200: BaseModel,
    },
)
def edit_phone_handler(request: HttpRequest):
    if request.method == "GET":
        return render_service.render_edit_phone_page(request)
    if request.method == "POST":
        return render_service.edit_phone(request)


@login_required
@router.get(
    "edit_bio/",
    response={
        200: BaseModel,
    },
)
@router.post(
    "edit_bio/",
    response={
        200: BaseModel,
    },
)
def edit_bio_handler(request: HttpRequest):
    if request.method == "GET":
        return render_service.render_edit_bio_page(request)
    if request.method == "POST":
        return render_service.edit_bio(request)


@login_required
@router.get(
    "name_display/",
    response={
        200: BaseModel,
    },
)
def name_display_handler(request: HttpRequest):
    return render_service.render_name_display(request)


@login_required
@router.get(
    "phone_display/",
    response={
        200: BaseModel,
    },
)
def phone_display_handler(request: HttpRequest):
    return render_service.render_phone_display(request)


@login_required
@router.get(
    "bio_display/",
    response={
        200: BaseModel,
    },
)
def bio_display_handler(request: HttpRequest):
    return render_service.render_bio_section(request)
