from django.db import models
# Create your models here.

class Price(models.Model):
    DBP = models.IntegerField(null=False)
    TBP = models.IntegerField(null=False)
    calc_price = models.FloatField(null=True, blank=True)
