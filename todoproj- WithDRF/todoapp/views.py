from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Task
from .serializers import TaskSerializer
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    # view all tasks
    tasks = Task.objects.all()
    context = TaskSerializer(tasks,many=True).data
    return Response(context)

@api_view(['GET'])
def details(request,pk):
    #view specific task
    task = Task.objects.get(id=pk)
    context =  TaskSerializer(task).data
    return Response(context)


@api_view(['POST'])
def create(request):
    serializer =TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update(request,pk):
    task = Task.objects.get(id=pk)
    serializer =TaskSerializer(data=request.data,instance=task)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
   

@api_view(['DELETE'])
def delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response({'message':f'task {pk}: Deleted'})



