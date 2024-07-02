from django.urls import path
from .import views

urlpatterns = [
    path('flan-list/', views.index, name='index')
]