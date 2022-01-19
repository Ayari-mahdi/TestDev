import requests
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    Articles = requests.get("http://127.0.0.1:8000/api/GetArticles").json()
    return render(request, 'index.html', {'Articles': Articles})




