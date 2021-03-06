import datetime

from django.db import models
from django.utils import timezone

# Create your models here.\

# Kunze Wu :   to generate our database,  just code in here , we don't need to edit database(mysql)  ,django will generate all code

# step :
# 1. edit  models.py
# 2.Terminal $ :  python manage.py makemigrations   # to generate .sql file to change database
#            $ :  python manage.py sqlmigrate ubs_project 0001  # to check the sql which was generated by django
# 3.Terminal $ :  python manage.py migrate

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text