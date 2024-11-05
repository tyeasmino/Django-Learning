from django.shortcuts import render
from task.models import TaskModel
from category.models import TaskCategoryModel


def index(request):
    task = TaskModel.objects.all()

    return render(request, 'index.html', {'task' : task}) 