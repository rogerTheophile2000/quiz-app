from django.forms import ModelForm
from .models import QuestionsModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']


class AddQuestion(ModelForm):
    class Meta:
        model = QuestionsModel
        fields = (
            "question",
            "option_one",
            "option_two",
            "option_three",
            "option_four",
            "answer",
        )
