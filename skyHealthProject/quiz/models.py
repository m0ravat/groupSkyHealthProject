from django.db import models
from core.models import User
# Create your models here.


class Session(models.Model):
    Quarter_Choices = [("Q1", "Q1"), ("Q2", "Q2"), ("Q3", "Q3"), ("Q4", "Q4")]
    sessionId = models.AutoField(primary_key=True)
    sessionYear = models.PositiveSmallIntegerField(max_length=4)
    sessionQuarter = models.CharField(choices=Quarter_Choices, max_length=2)

    class Meta:
        db_table = "Session"


class SessionAssignment(models.Model):
    sessionAssignId = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="hasSessions")
    sessionId = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True, related_name="isAssigned")
    additionalComments = models.TextField()

    class Meta:
        db_table = "Session_Assignment"

class Card(models.Model):
    cardId = models.AutoField(primary_key=True)
    cardName = models.CharField(max_length=100)
    cardDesc = models.TextField()

    class Meta:
        db_table= "Card"


class Vote(models.Model):
    Int_Choices = [(3, 3), (1, 1), (2, 2)]
    voteId = models.AutoField(primary_key=True)
    rating = models.IntegerField(choices=Int_Choices, max_length=1)
    progress = models.IntegerField(choices=Int_Choices, max_length=1)
    cardId = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, related_name="BelongsTo")
    sessionAssignId = models.ForeignKey(SessionAssignment, on_delete=models.SET_NULL, null=True, related_name="hasSession")
    class Meta:
        db_table = "Vote"