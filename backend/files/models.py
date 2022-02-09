from django.db import models

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    date_added = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

