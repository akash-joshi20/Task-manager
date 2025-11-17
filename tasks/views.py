from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})