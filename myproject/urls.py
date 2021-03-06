"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

#DRF
from rest_framework import routers
from notes.views import NoteViewSet, NoteList, NoteListed
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
# Notes router
notes_router = routers.SimpleRouter()

notes_router.register(
    r'notes',
    NoteViewSet,
    basename='note',
)

notes_router.register(
    r'usernotes',
    NoteViewSet,
    basename='usernotes',
)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("", views.homepage, name="homepage"),
    path("register", views.register, name="register"),
    path('vue-test', views.vue_test),
    path('auth_git', views.auth_git, name="auth_git"),
    path('authgit_callback', views.authgit_callback, name='authgit_callback'),
    path('auth_git_callback', views.auth_git_callback, name='auth_git_callback'),
    # API
    path('api/', include(notes_router.urls)),
    path('api/usernotes', NoteList.as_view(), name="usernotes"),
    path('api/usernotes/<int:pk>/', NoteListed.as_view()),

]   
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])