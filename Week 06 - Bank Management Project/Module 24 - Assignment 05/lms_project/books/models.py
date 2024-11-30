from django.db import models
from django.contrib.auth.models import User
from transactions.constants import TRANSACTION_TYPE

# Create your models here.
class BookCategoryModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    price = models.IntegerField() 
    category = models.ForeignKey(BookCategoryModel, on_delete=models.CASCADE)
    book_img = models.ImageField(upload_to='car/media/uploads/')

    def __str__(self):
        return f'{self.category} - {self.book_name} - ${self.price}'


class BookBorrowModel(models.Model):
    book_name = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='book')
    borrowed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE) 
    timestamp = models.DateTimeField(auto_now_add=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.borrowed_by} - {self.book_name.book_name}' 


# # class CommentModel(models.Model):
# #     car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
# #     name = models.CharField(max_length=50)
# #     email = models.EmailField()
# #     comment = models.TextField()
# #     commented_on = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f'Commented by - {self.name}'
        
