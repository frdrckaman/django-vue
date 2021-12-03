from django.urls import path
from .views import Users, Register

urlpatterns = [
    path('hello/', Users),
    path('register/', Register)
]
