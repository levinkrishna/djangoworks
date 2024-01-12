from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from task.models import Todos
from taskapi.serializers import TodoSerializer
from rest_framework.decorators import action

# Create your views here.


class TodoViewSetView(ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todos.objects.all()

#localhost:8000/api/v1/todos/pending
#methode:get
    @action(methods=["get"],detail=False)
    def pending(self,request,*args,**kwargs):
       qs=Todos.objects.filter(status=False)
       serializer=TodoSerializer(qs,many=True)
       return Response(data=serializer.data)
    
    @action(methods=["get"],detail=False)
    def completed(self,request,*args,**kwargs):
        qs=Todos.objects.filter(status=True)
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)
