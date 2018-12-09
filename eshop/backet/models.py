from django.db import models
from category.models import Laptop
# Create your models here.


class Backet(models.Model):
    product  = models.ForeignKey(Laptop , on_delete=models.CASCADE)

    def __str__(self):
        return self.product
