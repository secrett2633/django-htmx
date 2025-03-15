from django.shortcuts import render
from django.http import HttpRequest

from shared.views import get_navigation


class RenderService:
    @staticmethod
    def render_coin_page(request: HttpRequest):
        return render(request, "coin.html", {"navigation": get_navigation()})


render_service = RenderService()
