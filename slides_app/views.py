from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Task

# Create your views here.


def index(request):
    return HttpResponse("go fucking kill yourself || from slides_app")


def template_context_view(request):
    return render(request, 'slides_app/template.html', { 'name': 'slavery was a choice -Kanye West' })


def task_list(request):
    tasks = Task.objects.all()
    ctx = {
            'tasks': tasks
            }
    return render(request, 'task_list.html', ctx)


def task_detail(request, id):
    ctx = { 'task', Task.objects.get(id=id) }
    return render(request, 'task_detail.html', ctx)


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
