from django.shortcuts import render, redirect
from . import forms, models  
from django.contrib import messages
from django.urls import reverse_lazy 
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView


# Create your views here.
class addBookCategoryView(CreateView):
    model = models.BookCategoryModel
    form_class = forms.BookCategoryForm
    template_name = 'books/add_category.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Book Category added successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Book Category adding process failed!")
        return super().form_invalid(form)



class addBookDetailsView(CreateView):
    model = models.BookModel
    form_class = forms.BookDetailsForm
    template_name = 'books/add_details.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Book Details added successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Book Details adding process failed!")
        return super().form_invalid(form)
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        
        for field in form.fields.values():
            field.widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
    
        return form