"""
URL configuration for mytodo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from chatbot.urls import router as chatbot_router
from dashboard.urls import router as dashboard_router
from user.urls import router as user_router
from coin.urls import router as coin_router
from tasks.urls import router as task_router


base_api = NinjaAPI(title="todo", version="0.0.0")
base_api.add_router("", chatbot_router)
base_api.add_router("", dashboard_router)
base_api.add_router("", user_router)
base_api.add_router("", coin_router)
base_api.add_router("", task_router)

urlpatterns = [
    path("", base_api.urls),
    path("admin/", admin.site.urls),
]
