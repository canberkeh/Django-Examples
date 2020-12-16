from django.db import models

# Create your models here.
class Crypto(models.Model):
    coin = models.CharField(max_length=120, default='TR')
    symbol = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publish = models.DateField()

    # def __str__(self):
    #     return self.coin
