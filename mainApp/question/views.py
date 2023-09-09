from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
from django.shortcuts import render

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



