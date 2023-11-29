from django.shortcuts import render
from .models import MyModel

def index(request):
    data = MyModel.objects.all()
    return render(request, 'priem/index.html', {'data': data})
