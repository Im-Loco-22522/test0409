from django.db import models


class Question(models.Model):
    class CorrectAnswer(models.IntegerChoices):
        NO = 0, ("No")
        YES = 1, ("Yes")

    test = models.ForeignKey('test.Test', on_delete=models.CASCADE, related_name='test_question')
    text = models.CharField(max_length=256)
    correctAnswer = models.IntegerField(choices=CorrectAnswer.choices)

    class Meta:
        ordering = ['id']