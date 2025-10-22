from django.shortcuts import render

def hello_view(request):
    return render(request, 'pages/hello.html')

def signup_view(request):
    return render(request, 'pages/signup.html')

def about_view(request):
    return render(request, 'pages/about.html')