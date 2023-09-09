from django.db import models


class TestResult(models.Model):
    test = models.ForeignKey('test.Test', on_delete=models.CASCADE, related_name='tests')
    percent = models.FloatField(max_length=100.0)


    class Meta:
        ordering = ['id']