from django.urls import include, path

from .views import index, template_context_view

urlpatterns = [
        path('', index, name='index'),
        path('tce', template_context_view, name='template_context_view'),
    ]

app_name = "slides_app"
