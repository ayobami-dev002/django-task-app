from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        Task.objects.create(title=title, description = desc)
        return redirect('home')
    
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')
