from django.db import models

# Create your models here.

# define phone comments models.
class PhonespiderItem(models.Model):
    goods_title = models.CharField(max_length=200)
    comment_id = models.IntegerField()
    comment_date = models.DateField()
    comment_description = models.TextField()
    comment_sentiments = models.FloatField()