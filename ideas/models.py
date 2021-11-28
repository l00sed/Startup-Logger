from django.db import models

# Create your models here.


class Idea(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"
