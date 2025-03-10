from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from tasks.models import Task
from shared.views import get_navigation

def chatbot(request):
    tasks = Task.objects.all()
    return render(request, 'chatbot.html', {'tasks': tasks, 'navigation': get_navigation()})

chat_messages = []

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

chat_messages = []

@csrf_exempt
def chat_send(request):
    # user_message = request.POST.get("message")
    # if not user_message:
    #     return JsonResponse({"error": "메시지가 비어 있습니다."}, status=400)

    # # Add user message to the chat
    # chat_messages.append({"variant": "human", "text": user_message})
    return render(request, 'message.html', {"variant": "human", "text": "test"})
    return {"variant": "human", "text": "test"}

    # Respond with the updated message list in the form of HTML
    response_html = render(request, "message.html", {
        "messages": chat_messages
    }).content.decode("utf-8")

    return JsonResponse({"html": response_html})
