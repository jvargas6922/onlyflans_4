from django.shortcuts import render
from django.http import HttpResponse
from .models import Flan

# Create your views here.
def index(request):
    flans = Flan.objects.all()
    context ={'flans': flans}
    return render(request, 'flan/index.html', context)

#Clase 
#flan = Flan(name='flan de fresa')
#flan.save()

#flan = Flan(name='flan de durazno')