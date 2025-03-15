import requests
from requests import Response

from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import login, logout

from user.models import ServiceUser as User


class AuthService:
    @staticmethod
    def google_login(request: HttpRequest):
        client_id: str = settings.GOOGLE_CLIENT_ID
        redirect_uri: str = f"{settings.API_URL}/auth/google/callback"
        scope: str = "email profile"

        url: str = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"

        # HTMX 요청인 경우 리다이렉트 정보만 반환
        if request.headers.get("HX-Request"):
            return JsonResponse({"redirect": url}, headers={"HX-Redirect": url})

        # 일반 요청은 해당 URL로 리다이렉트
        return redirect(url)

    @staticmethod
    def google_callback(request: HttpRequest, code: str):
        token_url: str = "https://oauth2.googleapis.com/token"
        data: dict[str, str] = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": f"{settings.API_URL}/auth/google/callback",
            "grant_type": "authorization_code",
        }
        response: Response = requests.post(token_url, data=data)
        token_data: dict[str, str] = response.json()

        access_token: str = token_data.get("access_token")
        user_info_url: str = "https://www.googleapis.com/oauth2/v3/userinfo"
        headers: dict[str, str] = {"Authorization": f"Bearer {access_token}"}
        user_info_response: Response = requests.get(user_info_url, headers=headers)

        user_info: dict[str, str] = user_info_response.json()
        email: str = user_info.get("email")
        try:
            user: User = User.objects.get(email=email)
        except User.DoesNotExist:
            user: User = User.objects.create(
                username=email,
                email=email,
                first_name=user_info.get("given_name", ""),
                last_name=user_info.get("family_name", ""),
                provider="google",
            )

        login(request, user)
        return redirect("/dashboard")

    @staticmethod
    def logout_user(request: HttpRequest):
        logout(request)
        response = HttpResponse()
        response["HX-Redirect"] = "/"
        return response


auth_service = AuthService()
