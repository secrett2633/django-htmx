"""
ASGI config for mytodo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import re_path, path
from channels.routing import ProtocolTypeRouter, URLRouter

from tasks.consumers import TaskConsumer, SSEConsumer, ChatConsumer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shared.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": URLRouter([
        path('sse/', SSEConsumer.as_asgi()),
        path("ssechat/<str:message>/<str:chat_id>/", ChatConsumer.as_asgi()),
        re_path(r"", django_asgi_app)
    ]),

    "websocket": URLRouter([
        re_path(r"ws/tasks/$", TaskConsumer.as_asgi()),
    ]),
})