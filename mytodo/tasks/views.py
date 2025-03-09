import time, sys

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from tasks.models import Task
from django.views.decorators.csrf import csrf_exempt


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

@csrf_exempt
def add_task(request):
    title = request.POST.get('title')
    if title:
        task = Task.objects.create(title=title)
        return render(request, 'tasks/task_item.html', {'task': task})
    return HttpResponse(status=400)

@csrf_exempt
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return render(request, 'tasks/task_item.html', {'task': task})

@csrf_exempt
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return HttpResponse('')
