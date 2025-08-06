from django.shortcuts import render

def basic(request):
    return render(request, 'index.html')