from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = task.objects.all()

    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks, 'form':form}
    return render(request, 'app/list.html', context)

def updateTask(request, pk):
    task_item = task.objects.get(id=pk)

    form = TaskForm(instance=task_item)

    if request.method == 'POST':
            form = TaskForm(request.POST, instance=task_item)
            if form.is_valid():
                form.save()
                return redirect('/')
    context = {'form': form}
    return render(request, 'app/update_task.html', context)

def deleteTask(request, pk):
    item = task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'app/delete.html',context)
