from django.db import models


class Set(models.Model):
    spisock=models.CharField(max_length=500)
    image=models.ImageField(upload_to='image/fled')
    

class Surname(models.Model):
    name=models.ForeignKey (Set,on_delete=models.CASCADE)
    years= models.IntegerField()
    proff= models.CharField(max_length=500)
    sport=models.CharField(max_length=100)
    salary=models.FloatField(max_length=100000)
    



