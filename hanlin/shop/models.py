from django.db import models
from account.models import User
# Create your models here.

class Branch(models.Model):
    branchName = models.CharField(max_length=128, unique=True)
    url = models.CharField(max_length=128)
    
    def __str__(self):
        return self.branchName
    
class Plant(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    plantName = models.CharField(max_length=128)
    code = models.CharField(max_length=128, unique=True)
    price = models.IntegerField()
    inventory = models.IntegerField()
    pubDateTime = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=128)
    hot = models.BooleanField()
    discount = models.IntegerField()
    newPrice = models.IntegerField()
    buyes = models.ManyToManyField(User)
    
    def __str__(self):
        return self.branch.branchName +'-'+ self.plantName
    
    class Meta:
        ordering = ['-pubDateTime']
        