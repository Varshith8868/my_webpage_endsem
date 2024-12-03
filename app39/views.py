from django.shortcuts import render

def home(request):
    return render(request, 'app39/home.html')
