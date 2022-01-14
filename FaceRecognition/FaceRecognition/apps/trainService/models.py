from django.db import models

# Create your models here.

class UserRecognizer(models.Model):
    login = models.CharField(max_length=12)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.login