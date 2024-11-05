from django.shortcuts import render, redirect
from .forms import TaskCategoryForm

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()        
            return redirect('index')
    else:
        form = TaskCategoryForm()

    return render(request, 'category/add_category.html', {'form': form}) 