from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.db.models import Q

def task_list(request):
    query = request.GET.get('q')
    if query:
        tasks = Task.objects.filter(Q(title__icontains=query))
    else:
        tasks = Task.objects.all()

    # check for overdue tasks
    for task in tasks:
        task.check_and_update_overdue_status()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'query': query})

# this creates a new task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'form_title': 'Create Task'})

# this updates an existing task
def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'form_title': 'Update Task'})

# this deletes an existing task
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def task_confirm_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task, 'form_title': 'Delete Task'})