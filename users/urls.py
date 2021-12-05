from django.urls import path
from .views import Users, Register

urlpatterns = [
    path('users/', Users),
    path('register', Register)
]
