from django.shortcuts import render

from tasks.models import Task
from shared.views import get_navigation

def chatbot(request):
    tasks = Task.objects.all()
    return render(request, 'chatbot.html', {'tasks': tasks, 'navigation': get_navigation()})
