from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member #models.py
 
# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username']).exists():
            context = {'msg': 'That username is already taken'}
            return render(request, 'index.html', context)
        else:
            member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
            member.save()
            context = {'msg': 'Your registration has been successful, please log in!'}
            return render(request, 'login.html', context)
            #return redirect('login/')
    else:
        return render(request, 'index.html')
 
def login(request):
    return render(request, 'login.html')
 
def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            import requests
            import json
            url = "http://newsapi.org/v2/everything?q=apple&from=2020-10-16&to=2020-10-16&sortBy=popularity&apiKey=14d6ec672a5e4e72879c02d13c8a1b27"
            news_api_request = requests.get(url)
            api = json.loads(news_api_request.content)
            return render(request, 'home.html', {'api': api})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)