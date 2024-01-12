from django.urls import path
from reminder.views import SignUpView,SignInView,IndexView,TodoCreateView,TodoListView,TodoDetailView,TodoUpdateView


urlpatterns=[
    path("signup",SignUpView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin"),
    path("index",IndexView.as_view(),name="index"),
    path("add/",TodoCreateView.as_view(),name="add-todo"),
    path("all/",TodoListView.as_view(),name="list-todo"),
    path("<int:pk>/",TodoDetailView.as_view(),name="detail-todo"),
    path("<int:pk>/change",TodoUpdateView.as_view(),name="change-todo")
    


]