from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from .serializers import *
from .models import *

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def article_list(request):

    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True, context={'request': request})

    return JsonResponse(serializer.data, safe=False, status=200)