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
from tasks.views import *
from dashboard.views import *
from chatbot.views import *
from user.views import *
from shared.views import *
from coin.views import *

urlpatterns = [
    # Django 관리자 페이지
    path("admin/", admin.site.urls),
]

urlpatterns += [
    # Task 관련 URL
    path('', index, name='index'),
    path('add/', add_task, name='add_task'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    
    # Header 관련 URL
    path('mobile-menu/', mobile_menu, name='mobile_menu'),
]

urlpatterns += [
    # 인증 관련 URL
    path('signin/', signin_page, name='signin'),
    path('logout/', logout_user, name='logout'),
    
    # Google OAuth2 인증 URL
    path('auth/google/login/', google_login, name='google_login'),
    path('auth/google/callback/', google_callback, name='google_callback'),
    
    # 개인정보 처리 관련 URL
    path('pp', pp, name='pp'),
    path('tos', tos, name='tos')
]

urlpatterns += [
    # 유저 대시보드 관련 URL
    path('dashboard/', dashboard_page, name='dashboard'),
    
    # Edit views
    path('edit-name/', edit_name, name='edit_name'),
    path('edit-phone/', edit_phone, name='edit_phone'),
    path('edit-bio/', edit_bio, name='edit_bio'),
    
    # Display views (for cancel actions)
    path('name-display/', name_display, name='name_display'),
    path('phone-display/', phone_display, name='phone_display'),
    path('bio-section/', bio_section, name='bio_section'),
]

urlpatterns += [
    # Chatbot 관련 URL
    path('chatbot', chatbot, name='chatbot'),
    path('chatbot/send/', chat_send, name='chat_send'),
]

urlpatterns += [
    # Coin 관련 URL
    path('coin/', coin_page, name='coin'),
    path('load_market_data/', load_market_data, name='load_market_data'),
]