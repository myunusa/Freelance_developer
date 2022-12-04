from django.db import models

# Create your models here.

class ContactUs (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    project = models.CharField(max_length=255)
    description = models.TextField()

    def __str__ (self):
        return self.name

class FeedBack(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__ (self):
        return self.name
  

