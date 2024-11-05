from django.db import models

# Create your models here.
class MyModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date_time  = models.DateTimeField()
    duty_duration = models.DurationField()
    email = models.EmailField()
    rating = models.FloatField()
    salary = models.IntegerField()


    # big_auto_field = models.BigAutoField(primary_key=True)
    # big_integer_field = models.BigIntegerField()
    # binary_field = models.BinaryField()
    # boolean_field = models.BooleanField()
    # comma_separated_field = models.CharField(
    #     validators=[comma_separated_validator],
    #     max_length=255
    # )
    # date  = models.DateField()
    # decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    # file_field = models.FileField(upload_to='files/')
    # file_path_field = models.FilePathField(path='/path/to/files/')
    # generic_ip_address_field = models.GenericIPAddressField()
    # foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
    # image_field = models.ImageField(upload_to='images/')
    # json_field = models.JSONField()
    # many_to_many_field = models.ManyToManyField(OtherModel)
    # null_boolean_field = models.NullBooleanField()
    # one_to_one_field = models.OneToOneField(OtherModel, on_delete=models.CASCADE)
    # slug_field = models.SlugField()
    # small_integer_field = models.SmallIntegerField()
    # text_field = models.TextField()
    # time_field = models.TimeField()
    # url_field = models.URLField()
    # uuid_field = models.UUIDField()


