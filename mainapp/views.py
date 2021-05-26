from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


data = {
    'title': 'Главная страница!!!',
    'val': ['Some', 'Hello', '123'],
    'ob': {
        'car': 'BMW',
        'age': 18,
        'hobby': 'Foot'
    }
}

def index(request):
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
"""def about(request):
    return HttpResponse('Hi it is Hello')"""""
