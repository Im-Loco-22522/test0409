from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=256)

    class Meta:
        ordering = ['title']
