from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                          PermissionRequiredMixin)

from .models import Task, Group


class MainPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'tasks/main.html'


@login_required
def add_group(request):

    if request.method == 'POST':
        group_name = request.POST['group_name']
        group = Group(group_name=group_name)
        group.save()
        return HttpResponseRedirect('/tasks/board')
    else:
        return render(request, 'tasks/add_group.html')


def delete_group(request, id):
    try:
        group = Group.objects.get(id=id)
        group.delete()
        return HttpResponseRedirect('/tasks/board')
    except Task.DoesNotExist:
        return HttpResponseNotFound('<h2>The group not found</h2>')


@login_required
def tasks(request):
    groups = Group.objects.all()
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'groups': groups
    }
    return render(request, 'tasks/tasks.html', context)


def details(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task,
    }
    return render(request, 'tasks/details.html', context)


def get_group_context():
    groups = Group.objects.all()
    return groups


def add_task(request, id):
    group = Group.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        progress = group.group_name
        priority = request.POST['priority']
        task = Task(title=title, description=description, progress=progress, priority=priority)
        task.save()
        return HttpResponseRedirect('/tasks/board')
    else:
        current_group = Group.objects.get(id=id)
        return render(request, 'tasks/add_task.html', {'groups': get_group_context(),
                                                       'id':group.id,
                                                       'current_group': current_group.group_name})


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
            return render(request, 'tasks/edit.html',
                          {'task':task, 'groups':get_group_context})

    except Task.DoesNotExist:
        return HttpResponseNotFound('<h2>The task not found</h2>')


def index_plus(item):
    group_elem = Group.objects.all()
    group_list = []
    for group in Group.objects.all():
        group_list.append(group.group_name)
    try:
        res = group_list[group_list.index(item) + 1]
        return res
    except IndexError:
        return item



def move_to_next(request, id):
    try:
        task = Task.objects.get(id=id)
        task.progress = index_plus(task.progress)
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

