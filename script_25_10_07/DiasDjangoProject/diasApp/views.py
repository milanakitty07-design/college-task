from django.shortcuts import render

def hello_view(request):
    return render(request, 'diasApp/hello.html')

def signup_view(request):
    return render(request, 'diasApp/signup.html')