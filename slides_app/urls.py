from django.urls import include, path

from .views import index, template_context_view, task_list, task_detail

urlpatterns = [
        path('', index, name='index'),
        path('tce', template_context_view, name='template_context_view'),
        path('<int:id>', task_detail, name='task_detail')
    ]

app_name = "slides_app"
