from django.shortcuts import render

import random
from shared.views import get_navigation

def coin_page(request):
    return render(request, 'coin.html', {'navigation': get_navigation()})


def get_market_data(request):
    # Get filter parameters from request
    from_exchange = request.GET.get('from-exchange', 'upbit')
    to_exchange = request.GET.get('to-exchange', 'binance')
    search_term = request.GET.get('search-term', '')
    
    # Sorting parameters
    sort_field = request.GET.get('sort_field', 'volume')
    current_direction = request.GET.get('current_direction', '')
    
    # Determine sort direction
    sort_direction = 'desc'  # Default
    if sort_field and current_direction:
        if sort_field == request.GET.get('sort_field'):
            # Toggle direction if clicking the same field
            sort_direction = 'asc' if current_direction == 'desc' else 'desc'
    
    # Generate random market data
    coins = [
        {'symbol': 'BTC', 'korean_name': '비트코인', 'image_url': '/static/images/coins/btc.png'},
        {'symbol': 'ETH', 'korean_name': '이더리움', 'image_url': '/static/images/coins/eth.png'},
        {'symbol': 'XRP', 'korean_name': '리플', 'image_url': '/static/images/coins/xrp.png'},
        {'symbol': 'ADA', 'korean_name': '에이다', 'image_url': '/static/images/coins/ada.png'},
        {'symbol': 'SOL', 'korean_name': '솔라나', 'image_url': '/static/images/coins/sol.png'},
        {'symbol': 'DOT', 'korean_name': '폴카닷', 'image_url': '/static/images/coins/dot.png'},
        {'symbol': 'DOGE', 'korean_name': '도지코인', 'image_url': '/static/images/coins/doge.png'},
        {'symbol': 'AVAX', 'korean_name': '아발란체', 'image_url': '/static/images/coins/avax.png'},
        {'symbol': 'SHIB', 'korean_name': '시바이누', 'image_url': '/static/images/coins/shib.png'},
        {'symbol': 'MATIC', 'korean_name': '폴리곤', 'image_url': '/static/images/coins/matic.png'},
    ]
    
    markets = []
    
    for coin in coins:
        # Skip if not matching search term
        if search_term and search_term.lower() not in coin['symbol'].lower() and search_term.lower() not in coin['korean_name'].lower():
            continue
            
        # Generate random price data
        base_price = random.uniform(100, 100000) if coin['symbol'] != 'BTC' else random.uniform(50000000, 70000000)
        
        # Premium (can be positive or negative)
        premium_percent = random.uniform(-3.0, 3.0)
        
        # Calculate prices based on premium
        if from_exchange == 'upbit':  # Korean exchange generally has higher prices
            from_price = base_price * (1 + max(0, premium_percent/100))
            to_price = base_price
        else:
            from_price = base_price
            to_price = base_price * (1 + max(0, premium_percent/100))
            premium_percent = -premium_percent  # Reverse the premium direction
            
        # 24h price changes
        from_price_change24h = round(random.uniform(-10.0, 10.0), 2)
        to_price_change24h = round(random.uniform(-10.0, 10.0), 2)
        
        # Volume
        volume = random.uniform(1000000, 1000000000)
        
        # Format prices and volume
        def format_price(price):
            if price < 1:
                return f"{price:.6f}"
            elif price < 10:
                return f"{price:.4f}"
            elif price < 100:
                return f"{price:.2f}"
            else:
                # Format with commas for thousands separator
                return f"{int(price):,}"
                
        def format_volume(vol):
            if vol >= 1_000_000_000:
                return f"{vol/1_000_000_000:.2f}B"
            elif vol >= 1_000_000:
                return f"{vol/1_000_000:.2f}M"
            elif vol >= 1_000:
                return f"{vol/1_000:.2f}K"
            else:
                return f"{vol:.2f}"
        
        markets.append({
            'symbol': coin['symbol'],
            'korean_name': coin['korean_name'],
            'image_url': coin['image_url'],
            'price_gap_percent': round(premium_percent, 2),
            'from_price': from_price,
            'from_price_formatted': format_price(from_price),
            'from_price_change24h': from_price_change24h,
            'to_price': to_price,
            'to_price_formatted': format_price(to_price),
            'to_price_change24h': to_price_change24h,
            'volume': volume,
            'volume_formatted': format_volume(volume),
        })
    
    # Sort the data
    if sort_field == 'name':
        markets.sort(key=lambda x: x['korean_name'], reverse=(sort_direction == 'desc'))
    elif sort_field == 'premium':
        markets.sort(key=lambda x: x['price_gap_percent'], reverse=(sort_direction == 'desc'))
    elif sort_field == 'fromPrice':
        markets.sort(key=lambda x: x['from_price'], reverse=(sort_direction == 'desc'))
    elif sort_field == 'toPrice':
        markets.sort(key=lambda x: x['to_price'], reverse=(sort_direction == 'desc'))
    elif sort_field == 'volume':
        markets.sort(key=lambda x: x['volume'], reverse=(sort_direction == 'desc'))
    
    # Set exchange labels based on selection
    exchange_labels = {
        'upbit': '업비트',
        'bithumb': '빗썸',
        'coinone': '코인원',
        'binance': '바이낸스',
        'ftx': 'FTX',
        'kucoin': '쿠코인'
    }
    
    from_exchange_label = exchange_labels.get(from_exchange, from_exchange.capitalize())
    to_exchange_label = exchange_labels.get(to_exchange, to_exchange.capitalize())
    
    # Set base currency
    from_base = "KRW" if from_exchange in ['upbit', 'bithumb', 'coinone'] else "USDT"
    to_base = "KRW" if to_exchange in ['upbit', 'bithumb', 'coinone'] else "USDT"
    
    context = {
        'markets': markets,
        'from_exchange': from_exchange,
        'to_exchange': to_exchange,
        'from_exchange_label': from_exchange_label,
        'to_exchange_label': to_exchange_label,
        'from_base': from_base,
        'to_base': to_base,
        'search_term': search_term,
        'sort_state': {
            'field': sort_field,
            'direction': sort_direction
        }
    }
    return context

def load_market_data(request):
    context = get_market_data(request)
    return render(request, 'market_data.html', context)