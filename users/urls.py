from django.urls import path
from .views import (
    register, login, AuthenticatedUser, logout, PermissionAPIView, RoleViewSet, UserGenericAPIView,
    ProfileInfoAPIView, ProfilePasswordAPIVie
)

urlpatterns = [
    path('register', register),
    path('login', login),
    path('logout', logout),
    path('user', AuthenticatedUser.as_view()),
    path('permission', PermissionAPIView.as_view()),
    path('roles', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('users/info', ProfileInfoAPIView.as_view()),
    path('users/password', ProfilePasswordAPIVie.as_view()),
    path('users', UserGenericAPIView.as_view()),
    path('users/<str:pk>', UserGenericAPIView.as_view()),
]
