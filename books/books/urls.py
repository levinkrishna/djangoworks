"""
URL configuration for books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from task.views import BookCreateView,BookListView,BookDetailView,BookDeleateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("book/add",BookCreateView.as_view(),name="book-add"),
    path("book/list",BookListView.as_view(),name="book-list"),
    path("book/<int:pk>",BookDetailView.as_view(),name="book-detail"),
    path("book/<int:pk>/remove",BookDeleateView.as_view(),name="book-remove")
   
    
    
]
