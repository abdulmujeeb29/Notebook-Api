from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Note(models.Model):
    title =models.CharField(max_length =1000)
    body =models.CharField(max_length =10000)
    date_created =models.DateTimeField(null= True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self) :
        return self.title 
