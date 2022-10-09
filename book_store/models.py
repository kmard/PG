from django.db import models
from django.core.validators import  MinValueValidator,MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(max_length=100,null=True)
    is_bestselling = models.BooleanField(default=False)

    def get_absolute_url(self):
        return ''


    def __str__(self):
        return f'{self.title} / ({self.rating})'

