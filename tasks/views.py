from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by('-id')  # Newest first
    completed_tasks = tasks.filter(completed=True).count()
    total_tasks = tasks.count()
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'total_tasks': total_tasks
    })


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        category = request.POST.get(
            'category', 'General')  # Get category from form
        Task.objects.create(
            title=title, description=description, category=category)
        return redirect('task_list')
    else:
        # Handle GET request - redirect to task list
        return redirect('task_list')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description', '')
        task.category = request.POST.get('category', 'General')
        task.save()
        return redirect('task_list')
    else:
        # Handle GET request - redirect to task list
        return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
