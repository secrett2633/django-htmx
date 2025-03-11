from django.shortcuts import render

from tasks.models import Task
from shared.views import get_navigation

def chatbot(request):
    tasks = Task.objects.all()
    return render(request, 'chatbot.html', {'tasks': tasks, 'navigation': get_navigation()})

def chat_send(request):
    user_message = request.POST.get("message", "test")
    chat_id = request.session.get("chat_id", 1) + 1
    request.session["chat_id"] = chat_id    
    context = {"human_message": user_message, "chat_id": chat_id}
    print(context)
    return render(request, 'add_message.html', context)