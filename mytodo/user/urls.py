from django.http import HttpRequest
from ninja import Router

from user.service.auth import auth_service
from user.service.render import render_service
from shared.reponse import BaseModel


router = Router(tags=[""])


@router.get(
    "signin/",
    response={
        200: BaseModel,
    },
)
def signin_handler(request: HttpRequest):
    return render_service.render_signin_page(request)


@router.post(
    "/logout/",
    response={
        200: BaseModel,
    },
)
def logout_handler(request: HttpRequest):
    return auth_service.logout_user(request)


@router.post(
    "/google_login/",
    response={
        200: BaseModel,
    },
)
def google_login_handler(request: HttpRequest):
    return auth_service.google_login(request)


@router.get(
    "auth/google/callback/",
    response={
        200: BaseModel,
    },
)
def google_callback_handler(request: HttpRequest, code: str):
    return auth_service.google_callback(request, code)


@router.get(
    "pp/",
    response={
        200: BaseModel,
    },
)
def pp_handler(request: HttpRequest):
    return render_service.render_pp_page(request)


@router.get(
    "tos/",
    response={
        200: BaseModel,
    },
)
def tos_handler(request: HttpRequest):
    return render_service.render_tos_page(request)
