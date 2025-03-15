from django.shortcuts import render
from django.http import HttpRequest


class RenderService:
    @staticmethod
    def render_pp_page(request: HttpRequest):
        return render(request, "pp.html")

    @staticmethod
    def render_tos_page(request: HttpRequest):
        return render(request, "tos.html")

    @staticmethod
    def render_signin_page(request: HttpRequest):
        return render(request, "signin.html")


render_service = RenderService()
