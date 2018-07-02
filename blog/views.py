from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def test(request):
    return render(request, 'blog/test.html')