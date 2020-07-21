from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("<h1>welcome to homepage<h1>")

def sample(request):
    return render(request,"sample.html")
    
def sample1(request):
    return render(request,"directory/sample1.html",context={'data':"shivani",'name':"anwekar"}) 

def sample2(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/sample2.html",{'fruits':fruits})

def sample3(request):
    return render(request,"directory/sample3.html",{'a':10,'b':5})