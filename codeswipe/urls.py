"""
URL configuration for codeswipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup_1/', views.signup_1, name='signup_1'),
    path('signup_2/', views.signup_2, name='signup_2'),
    path('home/', views.home, name='home'),
    path('', views.root, name='root'),
    path('login/', views.login, name='login'),
    path('explore/', views.explore, name='explore'),
    path('swipe_right/<int:profile_id>/', views.swipe_right, name='swipe_right'),
    path('create_doubt_session/', views.create_coding_doubt_session, name='create_doubt_session'),
      # Root URL redirects to the home page
]

