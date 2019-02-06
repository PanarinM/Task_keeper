from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import TemplateView

from .models import Task


class MainPage(TemplateView):
    template_name = 'tasks/main.html'


def tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks.html', context)


def details(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task,
    }
    return render(request, 'tasks/details.html', context)


def add_task(request):

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        progress = request.POST['progress']
        priority = request.POST['priority']
        task = Task(title=title, description=description, progress=progress, priority=priority)
        task.save()
        return HttpResponseRedirect('/tasks/board')
    else:
        return render(request, 'tasks/add_task.html')


def edit(request, id):
    try:
        task = Task.objects.get(id=id)

        if request.method == 'POST':
            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.progress = request.POST.get('progress')
            task.priority = request.POST.get('priority')
            task.save()
            return HttpResponseRedirect('/tasks/board')
        else:
            return render(request, 'tasks/edit.html', {'task':task})
    except Task.DoesNotExist:
        return HttpResponseNotFound('<h2>The task not found</h2>')


def move_to_progress(request, id):
    try:
        task = Task.objects.get(id=id)
        task.progress = 'in progress'
        task.save()
        return HttpResponseRedirect('/tasks/board')
    except Task.DoesNotExist:
        return HttpResponseNotFound('<h2>The task not found</h2>')


def move_to_done(request, id):
    try:
        task = Task.objects.get(id=id)
        task.progress = 'done'
        task.save()
        return HttpResponseRedirect('/tasks/board')
    except Task.DoesNotExist:
        return HttpResponseNotFound('<h2>The task not found</h2>')


def delete(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponseRedirect('/tasks/board')
    except Task.DoesNotExist:
        return HttpResponseNotFound('<h2>The task not found</h2>')

