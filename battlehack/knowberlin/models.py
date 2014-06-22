from django.db import models
from django.contrib.auth.models import User

class QuestionsPack(models.Model):
    name = models.CharField(max_length=200)

class Topic(models.Model):
    name = models.CharField(max_length=200)
    questions_pack = models.ForeignKey(QuestionsPack)

class Question(models.Model):
    question = models.TextField()
    topic = models.ForeignKey(Topic)

class Answer(models.Model):
    answer = models.TextField()
    correct = models.BooleanField()
    question = models.ForeignKey(Question)

class Challenge(models.Model):
    user1 = models.ForeignKey(User, related_name='user1')
    user2 = models.ForeignKey(User, related_name='user2')
    user1_current_round = models.IntegerField()
    user2_current_round = models.IntegerField()

class Round(models.Model):
    challenge = models.ForeignKey(Challenge)
    topic = models.ForeignKey(Topic)
    #1th, 2th .... round
    number = models.IntegerField()
    user1_current_question = models.IntegerField()
    user2_current_question = models.IntegerField()

class RoundQuestion(models.Model):
    round = models.ForeignKey(Round)
    question = models.ForeignKey(Question)
    #1th, 2th .... question in round
    number = models.IntegerField()
    user1_answer = models.ForeignKey(Answer, null=True,
                                     related_name='user1_answer')
    user2_answer = models.ForeignKey(Answer, null=True,
                                     related_name='user2_answer')
