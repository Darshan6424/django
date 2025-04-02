from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.<h1>")

def test(request):
    return render(request, "polls/test.html")

def hello_page(request):
    return render(request,"polls/hello.html")