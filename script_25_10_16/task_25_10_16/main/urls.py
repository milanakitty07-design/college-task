from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('success/', views.success_view, name='success'),
    path('users/', views.users_view, name='users'),
    path('users/delete/<int:user_id>/', views.delete_user_view, name='delete_user'),
]
