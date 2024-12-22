from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task

@login_required
def index(request):
    """Домашняя страница приложения Learning Log"""
    tasks = Task.objects.filter(owner=request.user).order_by('deadline')
    context = {'tasks': tasks}
    return render(request, 'task/index.html', context)
@login_required
def new_task(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TaskForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('task:index')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'task/add_task.html', context)
@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:index')
    context = {'task': task, 'form': form}
    return render(request, 'task/edit_task.html', context)
@login_required
def del_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        raise Http404
    if request.method == 'POST':
        task.delete()
        return redirect('task:index')
    context = {'task': task}
    return render(request, 'task/confirm_delete.html', context)