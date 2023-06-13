from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=200,null=True)
    option_two = models.CharField(max_length=200,null=True)
    option_three = models.CharField(max_length=200,null=True)
    option_four = models.CharField(max_length=200,null=True)
    option_five = models.CharField(max_length=200,null=True)
    answer = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question