from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.db import IntegrityError

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        errors = []
        if not name:
            errors.append('Введите имя.')
        if not email:
            errors.append('Введите email.')
        if not password:
            errors.append('Введите пароль.')

        if errors:
            return render(request, 'main/signup.html', {'errors': errors, 'name': name, 'email': email})

        try:
            user = User(name=name, email=email, password=password)
            user.save()
        except IntegrityError:
            errors.append('Пользователь с таким email уже существует.')
            return render(request, 'main/signup.html', {'errors': errors, 'name': name, 'email': email})

        return redirect('success')

    return render(request, 'main/signup.html')

def success_view(request):
    return render(request, 'main/success.html')

def users_view(request):
    users = User.objects.all().order_by('name')
    return render(request, 'main/users.html', {'users': users})

def delete_user_view(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user.delete()
    return redirect('users')