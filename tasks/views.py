from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.


def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description', '')
        task.save()
        return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def toggle_task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
