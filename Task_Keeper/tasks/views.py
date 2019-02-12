from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, Group
from django.contrib.auth import get_user_model
from . import forms

User = get_user_model()


class MainPage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'tasks/main.html'


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


@login_required
def add_group(request):
    user = request.user
    if request.method == 'POST':
        group_name = request.POST['group_name']
        # group_order = request.POST['group_order']
        group = Group(user=user, group_name=group_name) #, group_order=group_order)
        group.save()
        return HttpResponseRedirect('/tasks/board')
    else:
        return render(request, 'tasks/add_group.html')


@login_required
def edit_group(request, id):
    try:
        group = Group.objects.get(id=id)
        tasks = Task.objects.filter(progress=group.group_name)
        if request.method == 'POST':
            group.group_name = request.POST.get('group_name')
            group.save()
            for task in tasks:
                task.progress = group.group_name
                task.save()
            return HttpResponseRedirect('/tasks/board')
        else:
            return render(request, 'tasks/group_edit.html',
                          {'group': group})

    except Group.DoesNotExist:
        return HttpResponseRedirect('/tasks/board')


@login_required
def delete_group(request, id):
    try:
        group = Group.objects.get(id=id)
        group_tasks = Task.objects.filter(progress=group.group_name)
        group.delete()
        group_tasks.delete()
        return HttpResponseRedirect('/tasks/board')
    except Task.DoesNotExist:
        return HttpResponseNotFound('<h2>The group not found</h2>')


@login_required
def tasks(request):
    user = request.user
    tasks_user = Task.objects.filter(user=user)
    groups = Group.objects.filter(user=user)
    context = {
        'tasks': tasks_user,
        'groups': groups
    }
    return render(request, 'tasks/tasks.html', context)


@login_required
def details(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task,
    }
    return render(request, 'tasks/details.html', context)


def get_group_context(user):
    groups = Group.objects.filter(user=user)
    return groups


@login_required
def add_task(request, id):
    user = request.user
    group = Group.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        progress = group.group_name
        priority = request.POST['priority']
        task = Task(user=user,
                    title=title,
                    description=description,
                    progress=progress,
                    priority=priority)
        task.save()
        return HttpResponseRedirect('/tasks/board')
    else:
        current_group = Group.objects.get(id=id)
        return render(request, 'tasks/add_task.html', {'groups': get_group_context(user),
                                                       'id':group.id,
                                                       'current_group': current_group.group_name})


@login_required
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
        return HttpResponseRedirect('/tasks/board')


def index_plus(item, user):
    group_elem = Group.objects.filter(user=user)
    group_list = []
    for group in Group.objects.filter(user=user):
        group_list.append(group.group_name)
    try:
        res = group_list[group_list.index(item) + 1]
        return res
    except IndexError:
        return item


@login_required
def move_to_next(request, id):
    user = request.user
    try:
        task = Task.objects.get(id=id)
        task.progress = index_plus(task.progress, user)
        task.save()
        return HttpResponseRedirect('/tasks/board')
    except Task.DoesNotExist:
        return HttpResponseRedirect('/tasks/board')


@login_required
def delete(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponseRedirect('/tasks/board')
    except Task.DoesNotExist:
        return HttpResponseRedirect('/tasks/board')

