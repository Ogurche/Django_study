from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_page (request):
    return render(request,'index.html')

def second_page (request):
    return HttpResponse('<h1>ЯЙЦА</h1>')