from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('signup/', views.signup_view, name='signup'),
    path('about/', views.about_view, name='about'),
]
