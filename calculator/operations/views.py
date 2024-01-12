from typing import Any
from django.shortcuts import render
from django.views.generic import View
from django import forms

class CalculatorForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

    def clean(self):
        self.cleaned_data=super().clean()
        n1=self.cleaned_data.get("num1")
        n2=self.cleaned_data.get("num2")
        if n1<1:
            msg="Please provide number >0"
            self.add_error("num1",msg)
        if n2<1:
            msg="Please provide number >0"
            self.add_error("num2",msg)

class RegistrationForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    phone=forms.CharField()
    username=forms.CharField()
    address=forms.CharField()

    def clean(self):
        self.cleaned_data=super().clean()
        phone=self.cleaned_data.get("phone")
        if len(phone)!=0:
            msg="invalid phone number"
            self.add_error("phone",msg)

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,"login.html",{"form":form})
        else:
            return render(request,"signup.html",{"form":form})
        
        

    
class ContactForm(forms.Form):
    subject=forms.CharField()
    Message=forms.CharField()
    sendeI=forms.EmailField()
    cc_myself=forms.BooleanField()

class ContactView(View):
    def get(self,request,*args,**kwargs):
        form=ContactForm()
        return render(request,"contact.html",{"form":form})

    

# Create your views here.

class HelloWorldView(View):
    def get(self,request,*args,**kwargs):
        print("printing hello world inside server")
        return render(request,"helloworld.html")
    

class GoodAfternoonView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"goodafternoon.html")
    
class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"morning.html")
    
class AdditionView(View):
    def get(self,request,*argd,**kwargs):
        form=CalculatorForm()
        return render(request,"add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=CalculatorForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=int(n1)+int(n2)
            return render(request,"add.html",{"result":res,"form":form})
        else:
            return render(request,"add.html",{"form":form})


class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        form=CalculatorForm()
        return render(request,"sub.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=CalculatorForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=int(n1)-int(n2)
            return render(request,"sub.html",{"result":res,"form":form})
        else:
            return render(request,"add.html",{"form":form})

        
class MultiplicationView(View):
    def get(sef,request,*args,**kwargs):
        form=CalculatorForm()
        return render(request,"multi.html",{"form":form}) 
    def post(self,request,*args,**kwargs):
        form=CalculatorForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=int(n1)*int(n2)
            return render(request,"multi.html",{"result":res,"form":form})
        else:
            return render(request,"add.html",{"form":form})

        # n1=request.POST.get("number1")
        # n2=request.POST.get("number2")
        # res=int(n1)*int(n2)
        # return render(request,"multi.html",{"result":res})
class DivisionView(View):
    def get(self,request,*args,**kwargs):
        form=CalculatorForm()
        return render(request,"divi.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=CalculatorForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=int(n1)/int(n2)
            return render(request,"divi.html",{"result":res,"form":form})
        else:
            return render(request,"add.html",{"form":form})
        # n1=request.POST.get("number1")
        # n2=request.POST.get("number2")
        # res=int(n1)/int(n2)
        # return render(request,"divi.html",{"result":res})
class CubeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"cube.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("number1")
        res=int(n1)**3
        return render(request,"cube.html",{"result":res})
class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fac.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("number1"))
        fact=1
        for i in range(1,n1+1):
            fact*=i
        return render(request,"fac.html",{"result":fact})


        


class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    

class OperationsView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"operations.html")
    def post(self,request,*args,**kwargs):
            n1=int(request.POST.get("num1"))
            n2=int(request.POST.get("num2"))
            requestdotPOST={"num1":100,"num2":200,"mul":""}
            if "add" in request.POST:
                res=n1+n2
            elif "sub" in request.POST:
                res=n1-n2
            elif "mul" in request.POST:
                res=n1*n2
            return render(request,"operations.html",{"result":res})
    


    # bmi

class BmiForm(forms.Form):
    weight=forms.IntegerField(label="enter weight in kg")
    height=forms.IntegerField(label="height in cm")   

    def clean(self):
        self.cleaned_data=super().clean()
        # print(self.cleaned_data)
        weight=self.cleaned_data.get("weight")
        height=self.cleaned_data.get("height")
        if weight >800:
            msg="invalid weight"
            self.add_error("weight",msg)
        if height >200:
            msg="invalid height"
            self.add_error("height",msg)


class BmiView(View):
    def get(self,request,*args,**kwargs):
        form=BmiForm()
        return render(request,"bmi.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BmiForm(request.POST)
        if form.is_valid():
            h_incm=form.cleaned_data.get("height")
            w_inkg=form.cleaned_data.get("weight")
            h_meter=h_incm/100
            bmi=w_inkg/(h_meter**2)
            return render(request,"bmi.html",{"result":bmi,"form":form})
        else:
            return render(request,"bmi.html",{"form":form})
        

class SalaryForm(forms.Form):
    basic=forms.IntegerField()
    hra=forms.IntegerField()
    sa=forms.IntegerField(label="special allowance")
    ta=forms.IntegerField(label="travelallowance")
    pf=forms.IntegerField()
    
    def clean(self):
        self.cleaned_data=super().clean()
        basic=self.cleaned_data.get("basic")
        hra=self.cleaned_data.get("hra")
        sa=self.cleaned_data.get("sa")
        ta=self.cleaned_data.get("ta")
        pf=self.cleaned_data.get("pf")

        if basic<=0:
            msg="basic pay must be > 0"
            self.add_error("basic",msg)
  

        


class SalaryView(View):
    def get(self,request,*args,**kwargs):
        form=SalaryForm()
        return render(request,"salary.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=SalaryForm(request.POST)
        if form.is_valid():
            basicpay=form.cleaned_data.get("basic")
            hra=form.cleaned_data.get("hra")
            spclallowance=form.cleaned_data.get("sa")
            travelallwnce=form.cleaned_data.get("ta")
            pf=form.cleaned_data.get("pf")
            netpay=int(basicpay)+int(hra)+int(spclallowance)+int(travelallwnce)-int(pf)
            return render(request,"salary.html",{"result":netpay,"form":form})
        else:
            return render(request,"salary.html",{"form":form})



