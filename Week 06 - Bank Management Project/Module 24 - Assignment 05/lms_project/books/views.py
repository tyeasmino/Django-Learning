from django.shortcuts import render, redirect, get_object_or_404
from . import forms, models  
from django.contrib import messages
from django.urls import reverse_lazy 
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView 
from transactions.models import Transaction
from transactions.constants import BORROW_BOOK, RETURN_BOOK

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


    
class bookDetailsView(DetailView):
    model = models.BookModel
    template_name = 'books/books_details.html'    
    pk_url_kwarg = 'id' 

    # def post(self, request, *args, **kwargs):
    #     comment_form = forms.CommentsForm(data= self.request.POST)
    #     car = self.get_object()

    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.car = car 
    #         new_comment.save() 
    #     return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        # comments = car.comments.all()  
        # comment_form = forms.CommentsForm()


        context['book'] = book 
        # context['comments'] = comments 
        # context['comment_form'] = comment_form
        return context


class borrowBookView(DetailView):
    model = models.BookModel
    template_name = 'books/books_details.html'    
    pk_url_kwarg = 'id' 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object

        
        if(self.request.user.account.balance >= book.price):
            self.request.user.account.balance = self.request.user.account.balance - book.price 
            book.quantity = book.quantity - 1
                
            self.request.user.account.save(
                update_fields=[
                    'balance'
                ]
            )
            book.save(
                update_fields=[
                    'quantity'
                ]
            )

            models.BookBorrowModel.objects.create(
                book_name = self.object,
                borrowed_by = self.request.user, 
                balance_after_transaction = self.request.user.account.balance,
                transaction_type = BORROW_BOOK
            )
        
            messages.success(self.request, "You have successfully borrowed this book!")
        else:
            messages.success(self.request, "Sorry!!! You don't have sufficent balance to borrowed this book!")

        
        context['book'] = book 

        context.update({
            'account': self.request.user.account,
            'book': book
        }) 
        return context 


class borrowReportView(ListView):
    model = models.BookBorrowModel 
    template_name = 'books/borrow_report.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        report = models.BookBorrowModel.objects.all()  


        context['report'] = report  
        return context
    

class returnBookView(DetailView):
    model = models.BookBorrowModel 
    template_name = 'books/borrow_report.html'    
    pk_url_kwarg = 'id' 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_borrow = self.object
        book = book_borrow.book_name  

        self.request.user.account.balance += book.price 
        book.quantity += 1
            
        self.request.user.account.save(
            update_fields=[
                'balance'
            ]
        )
        book.save(
            update_fields=[
                'quantity'
            ]
        )

        models.BookBorrowModel.objects.create(
            book_name = book,
            borrowed_by = self.request.user, 
            balance_after_transaction = self.request.user.account.balance,
            transaction_type = RETURN_BOOK
        )

        book_borrow.is_returned = True
        book_borrow.save(
            update_fields=[
                'is_returned'
            ]
        )
    
        messages.success(self.request, "You have successfully returned this book and refund is successful!") 
        report = models.BookBorrowModel.objects.all()  
        context['report'] = report  

        return context 

