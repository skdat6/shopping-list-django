from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'shopping_app/index.html')

def test(request):
    return render(request, 'shopping_app/test.html')