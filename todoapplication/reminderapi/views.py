from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from reminderapi.serializers import UserSerializer,Todoserializer
from reminder.models import Todos


from rest_framework import authentication
from rest_framework import permissions


# Create your views here.

class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class TodosViewSet(ViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def create(self,request,*args,**kwargs):
        serilaizer=Todoserializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save(user=request.user)
            return Response(data=serilaizer.data)
        else:
            return Response(data=serilaizer.errors)
        

    def list(self,request,*args,**kwargs):
        qs=Todos.objects.filter(user=request.user)
        serializer=Todoserializer(qs,many=True)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=Todoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    


        

        


        
