from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from ninja import Router

from dashboard.service.render import render_service
from shared.reponse import BaseModel


router = Router(tags=[""])


@router.get(
    "dashboard/",
    response={
        200: BaseModel,
    },
)
@login_required
def dashboard_handler(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("/signin")
    return render_service.render_dashboard_page(request)


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
@login_required
def edit_name_handler(request: HttpRequest):
    if request.method == "GET":
        return render_service.render_edit_name_page(request)
    if request.method == "POST":
        return render_service.edit_name(request)


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
@login_required
def edit_phone_handler(request: HttpRequest):
    if request.method == "GET":
        return render_service.render_edit_phone_page(request)
    if request.method == "POST":
        return render_service.edit_phone(request)


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
@login_required
def edit_bio_handler(request: HttpRequest):
    if request.method == "GET":
        return render_service.render_edit_bio_page(request)
    if request.method == "POST":
        return render_service.edit_bio(request)



@router.get(
    "name_display/",
    response={
        200: BaseModel,
    },
)
@login_required
def name_display_handler(request: HttpRequest):
    return render_service.render_name_display(request)



@router.get(
    "phone_display/",
    response={
        200: BaseModel,
    },
)
@login_required
def phone_display_handler(request: HttpRequest):
    return render_service.render_phone_display(request)


@router.get(
    "bio_display/",
    response={
        200: BaseModel,
    },
)
@login_required
def bio_display_handler(request: HttpRequest):
    return render_service.render_bio_section(request)
