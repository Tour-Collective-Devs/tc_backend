from django.db import models

class Employer(models.Model):
    name = models.CharField(default="", max_length=50)
    email = models.CharField(default="", max_length=50)
    password = models.CharField(default="", max_length=50)

    def __str__(self):
        return f'{self.name}'