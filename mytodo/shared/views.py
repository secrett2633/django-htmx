from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404

from tasks.models import Task


def get_navigation():
    """네비게이션 항목을 반환합니다."""
    return [
        {"name": "챗봇", "href": "/chatbot"},
        {"name": "커뮤니티", "href": "/community"},
    ]

def index(request):
    tasks = Task.objects.all()
    return render(request, 'shared/index.html', {'tasks': tasks, 'navigation': get_navigation()})

@csrf_exempt
def add_task(request):
    title = request.POST.get('title')
    if title:
        task = Task.objects.create(title=title)
        return render(request, 'shared/task_item.html', {'task': task})
    return HttpResponse(status=400)

@csrf_exempt
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return render(request, 'shared/task_item.html', {'task': task})

@csrf_exempt
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return HttpResponse('')

def mobile_menu(request):
    """모바일 메뉴를 렌더링합니다."""
    context = {
        'navigation': get_navigation(),
        'user': request.user,
    }
    return render(request, 'shared/mobile_menu.html', context)





