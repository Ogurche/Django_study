from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index_page (request):
    return render(request,'index.html')

def second_page (request, add_arg):
    return HttpResponse(f'<h1>ЯЙЦА</h1><p>{add_arg}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')