from django.db import models
from django.core.validators import  MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} / ({self.last_name})'


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    # author = models.CharField(max_length=100,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='',null=False,db_index=True,blank=True)

    def get_absolute_url(self):
        return reverse('book',args=[self.id])

    def get_absolute_slug(self):
        return reverse('book_slug',args=[self.slug])

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.title} / ({self.rating})'

