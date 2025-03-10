import requests

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, logout

from user.models import ServiceUser as User
from shared.views import get_navigation


@csrf_exempt
def google_login(request):
    """Google OAuth 로그인 URL 반환"""
    client_id = settings.GOOGLE_CLIENT_ID
    redirect_uri = f"{settings.API_URL}/auth/google/callback"
    scope = "email profile"
    
    url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"
    
    # HTMX 요청인 경우 리다이렉트 정보만 반환
    if request.headers.get('HX-Request'):
        return JsonResponse({
            'redirect': url
        }, headers={'HX-Redirect': url})
    
    # 일반 요청은 해당 URL로 리다이렉트
    return redirect(url)

def google_callback(request):
    """Google OAuth 콜백 처리"""
    code = request.GET.get('code')
    
    # 1. 코드를 사용하여 액세스 토큰 획득
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        'code': code,
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        'redirect_uri': f"{settings.API_URL}/auth/google/callback",
        'grant_type': 'authorization_code'
    }
    
    print(data)
    response = requests.post(token_url, data=data)
    token_data = response.json()
    
    print(response)
    access_token = token_data.get('access_token')
    
    # 2. 액세스 토큰으로 사용자 정보 가져오기
    user_info_url = "https://www.googleapis.com/oauth2/v3/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}
    
    user_info_response = requests.get(user_info_url, headers=headers)
    user_info = user_info_response.json()
    print(user_info)
    # 3. 사용자 정보로 Django 사용자 생성 또는 조회
    email = user_info.get('email')

    # 이메일로 사용자 조회, 없으면 새로 생성
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # 새 사용자 생성
        user = User.objects.create(
            username=email,  # 이메일을 사용자명으로 사용
            email=email,
            first_name=user_info.get('given_name', ''),
            last_name=user_info.get('family_name', ''),
            provider='google',
        )
    
    # 4. Django의 로그인 함수를 사용하여 사용자 로그인
    login(request, user)
    # 5. 홈 페이지로 리다이렉트
    return redirect('/dashboard')

def logout_user(request):
    logout(request)
    response = HttpResponse()
    response['HX-Redirect'] = '/'
    return response

def pp(request):
    return render(request, "pp.html")

def tos(request):
    return render(request, "tos.html")

def signin_page(request):
    return render(request, 'signin.html')