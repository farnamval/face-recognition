from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='persons')
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name


class PersonImages(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    images = models.FileField(upload_to='temp/person-image', max_length=100)

class PersonA(models.Model):
    name = models.CharField(blank=False, max_length=100)
    images = models.FileField(upload_to='temp/person-image', max_length=100)

    def __str__(self):
        return self.name