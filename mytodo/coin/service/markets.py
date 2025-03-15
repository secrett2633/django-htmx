import random
from typing import List, Dict, Any

from django.shortcuts import render
from django.http import JsonResponse, HttpRequest


class MarketsService:
    @staticmethod
    def get_market_data(request: HttpRequest):
        coins: list[dict] = [
            {
                "symbol": "BTC",
                "korean_name": "비트코인",
                "image_url": "/static/images/coins/btc.png",
            },
            {
                "symbol": "ETH",
                "korean_name": "이더리움",
                "image_url": "/static/images/coins/eth.png",
            },
            {
                "symbol": "XRP",
                "korean_name": "리플",
                "image_url": "/static/images/coins/xrp.png",
            },
            {
                "symbol": "ADA",
                "korean_name": "에이다",
                "image_url": "/static/images/coins/ada.png",
            },
            {
                "symbol": "SOL",
                "korean_name": "솔라나",
                "image_url": "/static/images/coins/sol.png",
            },
            {
                "symbol": "DOT",
                "korean_name": "폴카닷",
                "image_url": "/static/images/coins/dot.png",
            },
            {
                "symbol": "DOGE",
                "korean_name": "도지코인",
                "image_url": "/static/images/coins/doge.png",
            },
            {
                "symbol": "AVAX",
                "korean_name": "아발란체",
                "image_url": "/static/images/coins/avax.png",
            },
            {
                "symbol": "SHIB",
                "korean_name": "시바이누",
                "image_url": "/static/images/coins/shib.png",
            },
            {
                "symbol": "MATIC",
                "korean_name": "폴리곤",
                "image_url": "/static/images/coins/matic.png",
            },
        ]

        markets: List[Dict[str, Any]] = []

        for coin in coins:
            premium_percent: float = random.uniform(-3.0, 3.0)
            from_price_change24h: float = round(random.uniform(-10.0, 10.0), 2)
            to_price_change24h: float = round(random.uniform(-10.0, 10.0), 2)
            volume: float = random.uniform(1000000, 1000000000)

            markets.append(
                {
                    "symbol": coin["symbol"],
                    "korean_name": coin["korean_name"],
                    "image_url": coin["image_url"],
                    "price_gap_percent": round(premium_percent, 2),
                    "from_price_change24h": from_price_change24h,
                    "to_price_change24h": to_price_change24h,
                    "volume": volume,
                    "volume_formatted": markets_service.format_volume(volume),
                }
            )

        context: dict[str, list[dict]] = {"markets": markets}
        return context

    @staticmethod
    def market_update(request: JsonResponse):
        markets = markets_service.get_market_data(request)
        return JsonResponse(markets)

    @staticmethod
    def format_price(price: float):
        if price < 1:
            return f"{price:.6f}"
        elif price < 10:
            return f"{price:.4f}"
        elif price < 100:
            return f"{price:.2f}"
        else:
            return f"{int(price):,}"

    @staticmethod
    def format_volume(vol: float):
        if vol >= 1_000_000_000:
            return f"{vol/1_000_000_000:.2f}B"
        elif vol >= 1_000_000:
            return f"{vol/1_000_000:.2f}M"
        elif vol >= 1_000:
            return f"{vol/1_000:.2f}K"
        else:
            return f"{vol:.2f}"

    @staticmethod
    def load_market_data(request: HttpRequest):
        context: dict[str, Any] = markets_service.get_market_data(request)
        return render(request, "market_data.html", context)


markets_service = MarketsService()
