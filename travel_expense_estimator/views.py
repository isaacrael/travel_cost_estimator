from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def estimator(request):
    return render(request, 'estimator.html')
