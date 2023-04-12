from django.db import models

class Surname(models.Model):
    name=models.CharField(max_length=100)
    years= models.IntegerField()
    proff= models.CharField(max_length=500)
    sport=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/fled')




