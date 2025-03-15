from django.http import HttpRequest
from ninja import Router

from coin.service.render import render_service
from coin.service.markets import markets_service
from shared.reponse import BaseModel


router = Router(tags=[""])


@router.get(
    "coin/",
    response={
        200: BaseModel,
    },
)
def coin_handler(request: HttpRequest):
    return render_service.render_coin_page(request)


@router.get(
    "load_market_data/",
    response={
        200: BaseModel,
    },
)
def load_market_data_handler(request: HttpRequest):
    return markets_service.load_market_data(request)


@router.get(
    "market_update/",
    response={
        200: BaseModel,
    },
)
def market_update_handler(request: HttpRequest):
    return markets_service.market_update(request)
