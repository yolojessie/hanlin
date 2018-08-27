from django.db import models
from account.models import User
from shop.models import Plant
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    totalPrice = models.IntegerField()
    payMethod = models.CharField(max_length=128)
    pubDateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name +'-'+ self.plantName
    
    class Meta:
        ordering = ['-pubDateTime']
    
    