from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
    return render(request,'website/index.html' )

def task_view(request):
    # Example dynamic data
    tasks = [
        {'name': 'Task 1', 'description': 'Complete Django project'},
        {'name': 'Task 2', 'description': 'Prepare presentation'},
        {'name': 'Task 3', 'description': 'Submit assignment'},
    ]
    return render(request, 'website/task.html', {'tasks': tasks})