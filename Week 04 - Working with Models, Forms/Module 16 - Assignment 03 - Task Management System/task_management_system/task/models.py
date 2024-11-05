from django.db import models
from category.models import TaskCategoryModel

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=50)
    task_description = models.TextField(max_length=200)
    task_assign_date = models.DateField(auto_now=True)
    task_category = models.ManyToManyField(TaskCategoryModel) 
    task_is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title
    