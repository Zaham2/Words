from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'a': "batates mehammara"}
    return render(request,'homepage.html', context)

def count(request):
    return render(request,'count.html')

def about(request):
    text = request.GET['aboutName']
    context = { 'theNameIwantToUse' : text}
    return render(request,'about.html',context)