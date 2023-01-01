from django.db import models


# Create your models here.
class Product(models.Model):
    pr_name = models.CharField(max_length=100)
    pr_amount = models.IntegerField()
    pr_cost = models.DecimalField(decimal_places=2, max_digits=7)
    pr_description = models.CharField(max_length=1000, blank=True, null=True)
    pr_image = models.FileField(blank=True, null=True)
    pr_date = models.DateTimeField(auto_now_add=True)
