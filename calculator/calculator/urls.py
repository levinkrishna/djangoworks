"""
URL configuration for calculator project.

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
from operations.views import HelloWorldView,GoodAfternoonView,GoodMorningView,AdditionView,SubtractionView,MultiplicationView,DivisionView,CubeView,FactorialView,IndexView,OperationsView,SignUpView,ContactView,BmiView,SalaryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("helloworld/",HelloWorldView.as_view(),name="helloworld"),
    path("goodafter/",GoodAfternoonView.as_view(),name="afternoon"),
    path("morning/",GoodMorningView.as_view(),name="morning"),
    path("add/",AdditionView.as_view(),name="addition"),
    path("sub/",SubtractionView.as_view(),name="subtraction"),
    path("multi/",MultiplicationView.as_view(),name="multiplication"),
    path("div/",DivisionView.as_view(),name="division"),
    path("cube/",CubeView.as_view(),name="cube"),
    path("fac/",FactorialView.as_view(),name="factorial"),
    path("",IndexView.as_view(),name="home"),
    path("operations/",OperationsView.as_view(),name="operations"),
    path("registration/",SignUpView.as_view(),name="signup"),
    path("contact/",ContactView.as_view(),name="contact"),
    path("bmi/",BmiView.as_view(),name="bmi"),
    path("salary/",SalaryView.as_view(),name="salary")
]
