from django.db import models
from django.core.validators import  MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Adress(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.city}/{self.street}/{self.postal_code}'
    
    class Meta:
        # verbose_name_plural = ''
          verbose_name='Adress Entries' 
        

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Adress,on_delete=models.CASCADE,null=True)
    # favorite_created_book=models.ForeignKey(Book, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f'{self.first_name} / ({self.last_name}) : {self.address}'

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

