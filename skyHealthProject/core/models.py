from django.db import models

# Create your models here.
class User(models.Model):
    Role_Choices = [
        ("Engineer", "Engineer"),
        ("teamLeader", "Team Leader"),
        ("deptLeader", "Department Leader"),
        ("seniorManager", "Senior Manager"),
    ]
    username = models.CharField(max_length=50, primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    role = models.CharField(choices=Role_Choices, max_length=50)
    password = models.CharField(max_length=128)
    class Meta:
        db_table = "User"


class Department (models.Model):
    Dept_Choices = []
    deptName = models.CharField(max_length=50, primary_key=True)
    seniorManager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Managed_By")
    deptLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Led_By")
    class Meta:
        db_table = "Department"


class Team (models.Model):
    Team_Choices = []
    teamName = models.CharField(max_length=50, primary_key=True)
    teamLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Led_Teams")
    deptName = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="Led_Departments")
    class Meta:
        db_table = "Team"

#The code below was done by Iqra Shah (w1973224)
class Card(models.Model):
    cardId = models.CharField(max_length=10, primary_key=True)
    cardName = models.CharField(max_length=100)
    cardDesc = models.TextField()
    class Meta:
        db_table = "Card"


class Session(models.Model):
    sessionId = models.CharField(max_length=10, primary_key=True)
    sessionYear = models.CharField(max_length=10)
    sessionQuarter = models.CharField(max_length=10)
    class Meta:
        db_table = "Session"


class SessionAssignment(models.Model):
    assignId = models.CharField(max_length=10, primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    sessionId = models.ForeignKey(Session, on_delete=models.CASCADE)
    additionalComments = models.TextField(null=True, blank=True)
    class Meta:
        db_table = "SessionAssignment"


class Vote(models.Model):
    voteId = models.CharField(max_length=10, primary_key=True)
    rating = models.IntegerField()
    progress = models.IntegerField()
    cardId = models.ForeignKey(Card, on_delete=models.CASCADE)
    sessionId = models.ForeignKey(Session, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    assignId = models.ForeignKey(SessionAssignment, on_delete=models.CASCADE)
    class Meta:
        db_table = "Vote"
