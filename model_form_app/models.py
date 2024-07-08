from django.db import models

# Create your models here.
class form(models.Model):
        name= models.CharField(max_length=30)
        big_integer_field = models.BigIntegerField()
        binary_field = models.BinaryField()
        date_field = models.DateField()
        date_time_field = models.DateTimeField()
        decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
        email_field = models.EmailField()
        integer_field = models.IntegerField()
        small_integer_field = models.SmallIntegerField()
        text_field = models.TextField()
        time_field = models.TimeField()