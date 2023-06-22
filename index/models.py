from django.db import models

# Create your models here.


class register(models.Model):
    Fullname = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.Fullname
