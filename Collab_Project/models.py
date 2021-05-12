from django.db import models


# Create your models here.
class Challan(models.Model):
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    lisencenumber = models.CharField(max_length=30)
    vehiclenumber = models.CharField(max_length=30)
    vehicletype= models.CharField(max_length=30)
    createdby = models.CharField(max_length=30)

    def __str__(self):
        return self.lisencenumber

class Queries(models.Model): 
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Message = models.TextField()

    def __str__(self):
        return self.Name

class Help(models.Model):
    title = models.CharField(max_length=30)
    head = models.TextField()
    desc = models.TextField()
 

    def __str__(self):
        return self.title

class Home(models.Model):
    title = models.CharField(max_length=30)
    slidingtext = models.TextField()

    def __str__(self):
        return self.title