from django.shortcuts import render

from .models import Question
# Create your views here.

def view_questions(request):
    questions = Question.objects.all()
    return render(request, "displayQuestions.html",{'questions' : questions})