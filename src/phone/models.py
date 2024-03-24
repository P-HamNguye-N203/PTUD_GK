from django.db import models

# Create your models here.
class Phone(models.Model):
    phoneNumber = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'phone'

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user'
