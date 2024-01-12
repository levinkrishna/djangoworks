from django.shortcuts import render,redirect
from reminder.forms import RegistrationForm
from django.views.generic import View

# Create your views here.

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
