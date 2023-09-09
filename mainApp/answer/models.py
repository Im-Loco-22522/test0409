from django.db import models


class Answer(models.Model):
    class CorrectAnswer(models.IntegerChoices):
        NO = 0
        YES = 1

    question = models.ForeignKey('question.Question', on_delete=models.CASCADE, related_name='questions')
    testResult = models.ForeignKey('testresult.testResult', on_delete=models.CASCADE, related_name='testresults')
    answer = models.IntegerField(choices=CorrectAnswer.choices)

    class Meta:
        ordering = ['id']