from django.urls import path

from .views import index

urlpatterns = [
        path('', index, name='index')
    ]

# I suppose this is "creating" the namespace
app_name = "slides_app"

