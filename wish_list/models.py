from django.db import models
from django.contrib.auth.models import User





class WisherList(models.Model):
    name = models.CharField(max_length=120)
    url = models.CharField(max_length=120,blank=True,null=True)
    time = models.DateTimeField( auto_now_add=True,blank=True,null=True)
    image = models.ImageField(null=True,blank=True)

    wisher = models.ForeignKey(User, on_delete=models.CASCADE)
