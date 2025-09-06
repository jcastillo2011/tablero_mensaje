from django.shortcuts import render
from .models import Task
from django.views.generic import ListView #me mpermite crear vistas basadas en clases

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'tasks_list.html'
   
