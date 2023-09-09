from django.db import models


class Question(models.Model):
    class CorrectAnswer(models.IntegerChoices):
        NO = 0
        YES = 1

    test = models.ForeignKey('test.Test', on_delete=models.CASCADE, related_name='test_question')
    text = models.CharField(max_length=256)
    correct_answer = models.IntegerField(choices=CorrectAnswer.choices)

    class Meta:
        ordering = ['id']