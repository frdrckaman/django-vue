from django.urls import path
from .views import register, login, AuthenticatedUser, logout, PermissionApiView, RoleViewSet

urlpatterns = [
    path('register', register),
    path('login', login),
    path('logout', logout),
    path('user', AuthenticatedUser.as_view()),
    path('permission', PermissionApiView.as_view()),
    path('roles', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
