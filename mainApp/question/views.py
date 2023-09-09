from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
from django.shortcuts import render

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def index(request):
    return render(request, 'question/index.html')


