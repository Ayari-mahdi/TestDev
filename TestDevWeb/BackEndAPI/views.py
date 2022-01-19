from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from BackEndAPI.models import Articles
from BackEndAPI.serializers import ArticlesSerializer

# Create your views here.

@csrf_exempt
def getapi(request):
    if request.method =='GET':
        Article = Articles.objects.all()
        ArticleSerializer = ArticlesSerializer(Article, many=True)
        return JsonResponse(ArticleSerializer.data, safe=False)


@csrf_exempt
def addapi(request):
    if request.method == 'POST':
        article_data = JSONParser().parse(request)
        articleserializer = ArticlesSerializer(data=article_data)
        if articleserializer.is_valid():
            articleserializer.save()
        return JsonResponse(articleserializer.data, safe=False)
