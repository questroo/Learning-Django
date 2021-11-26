from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()

    def __str__(self):
        return self.firstname