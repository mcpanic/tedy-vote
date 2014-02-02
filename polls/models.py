from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=32, unique=True)
    choice_desc = models.CharField(max_length=200)
    proposer = models.EmailField()
    votes = models.IntegerField(default=0)

class Voter(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)
    email = models.EmailField()
    subscription = models.BooleanField(default=True) 
