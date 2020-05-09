from django.urls import path, include
from .views import hiAPI

urlpatterns = [
    path('hi/', hiAPI)
]