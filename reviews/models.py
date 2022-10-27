from django.db import models

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField(max_length=200)
    raiting = models.IntegerField()



