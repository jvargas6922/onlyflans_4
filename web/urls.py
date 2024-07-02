from django.urls import path
from .import views

urlpatterns = [
    path('web-list/', views.index, name='index_web')
]

#/ => raiz
#/web/web-list => web-list
#/flan/flan-list => flan-list