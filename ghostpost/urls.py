"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from ghostpost_app import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('boasts/', views.boasts),
    path('roasts/', views.roasts),
    path('sorted/', views.sorted_view),
    path('add_post/', views.add_post_view),
    path('post/<int:id>/', views.sorted_view),
    path('upvote/<int:id>/', views.upVote),
    path('downvote/<int:id>/', views.downVote),
    path('admin/', admin.site.urls),
]
