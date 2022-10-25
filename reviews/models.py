from django.db import models

class Review(models.Model):
    user_name = models.CharField()
    review_text = models.CharField()
    raiting = models.IntegerField()



