from django.db import models

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
    

# # class CommentModel(models.Model):
# #     car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
# #     name = models.CharField(max_length=50)
# #     email = models.EmailField()
# #     comment = models.TextField()
# #     commented_on = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f'Commented by - {self.name}'
        
