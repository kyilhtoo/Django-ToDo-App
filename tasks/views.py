from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect
from .models import Tasks
from .forms import TaskForm


class TasksList(ListView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = 'task_list.html'


def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task_input = form.cleaned_data.get("task_input")
            detail_input = form.cleaned_data.get("detail_input")
            task = Tasks.objects.create(task_name=task_input, task_detail=detail_input)
            task.save()
    return redirect('list_task')


def deleteTask(request, pk):
    if request.method == "POST":
        task = Tasks.objects.get(pk=pk).delete()
    return redirect('list_task')
