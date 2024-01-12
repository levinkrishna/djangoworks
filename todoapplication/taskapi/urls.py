from django.urls import path
from taskapi import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("v1/todos",views.TodoViewSetView,basename="v1todos")


urlpatterns=[

]+router.urls