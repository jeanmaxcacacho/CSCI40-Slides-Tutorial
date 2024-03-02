from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("go fucking kill yourself || from slides_app")


def template_context_view(request):
    return render(request, 'slides_app/template.html', {'name':'slavery was a choice -Kanye West'})
