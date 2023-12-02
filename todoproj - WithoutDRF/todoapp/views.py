from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json


def index(request):
    # view all tasks
    tasks = Task.objects.all()
    context = [{'id':task.id, 'title':task.title,'isComplete':task.isComplete} for task in tasks]
    return JsonResponse(context,safe=False)


def details(request,pk):
    #view specific task
    task = Task.objects.get(id=pk)
    context = {'id':task.id, 'title':task.title,'isComplete':task.isComplete}
    return JsonResponse(context,safe=True)


@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        isComplete = data.get('isComplete')

        task = Task(title=title,isComplete=isComplete)
        task.save()

        return JsonResponse({'message':'task created'})
    return HttpResponse("Method Not Allowed")


    

@csrf_exempt
def update(request,pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        print(task.title,task.id,task.isComplete)
        data = json.loads(request.body)
        title = data.get('title')
        isComplete = data.get('isComplete')
        print(title,isComplete,'from upated')

        task.title = title
        task.isComplete = isComplete
        task.save()

        return JsonResponse({'message':f'task {pk}: Updated'})
    return HttpResponse("Method Not Allowed")
        



def delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return JsonResponse({'message':f'task {pk}: Deleted'})



