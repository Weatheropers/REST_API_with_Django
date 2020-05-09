from django.urls import path, include
from .views import hiAPI
from .views import gu
from .views import header

urlpatterns = [
    path('hi/', hiAPI),
    path('<int:number>', gu),
]