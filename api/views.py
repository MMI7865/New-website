from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .serializers import *
from .models import *
from .forms import *

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            if 'profile_pic' in request.FILES:
                user.profile_pic = request.FILES['profile_pic']
                
            user.save()
            return redirect('home')
    else:
        form = SignUpForm()
        
    return render(request, 'api/spa/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        print("Im here")
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Attempting to authenticate user: {username} with password: {password}")
            user = authenticate(request, username=username, password=password)
            print("Im here2")
            if user is not None:
                login(request, user)
                print("Im here3")
                return redirect('home')
        print("Im here4")

        return render(request, 'api/spa/login.html', {
                    'form': form,
                    'error': 'Invalid username or password. Please try again.',
                })
    else:
        form = LoginForm()
        print("Im here5")
    return render(request, 'api/spa/login.html', {'form': form})

def article_list(request):

    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True, context={'request': request})

    return JsonResponse(serializer.data, safe=False, status=200)

def user_profile(request, username):
    user = User.objects.get(username=username)
    serializer= UserSerializer(user, context={'request': request})

    return JsonResponse(serializer.data, safe=False, status=200)