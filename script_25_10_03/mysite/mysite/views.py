from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def second_page(request):
    return render(request, 'second_page.html')
