from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phonenumber = models.IntegerField(default=0)
    email = models.EmailField()
    service = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.lastname

class ImageModel(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

