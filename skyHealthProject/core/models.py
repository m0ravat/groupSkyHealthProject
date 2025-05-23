# All code below is the work of Iqra Shah (1973224) - Muhammad Ravat (w1984454) created table classes
from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password, check_password
import re

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
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class Department(models.Model):
    Dept_Choices = []
    deptName = models.CharField(max_length=50, primary_key=True)
    seniorManager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Managed_By")
    deptLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Led_By")

    class Meta:
        db_table = "Department"

    def __str__(self):
        return re.sub(r'(?<!^)(?=[A-Z])', ' ', self.deptName).title()

class Team(models.Model):
    Team_Choices = []
    teamName = models.CharField(max_length=50, primary_key=True)
    teamLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Led_Teams")
    deptName = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="Led_Departments")

    class Meta:
        db_table = "Team"

    def __str__(self):
        return re.sub(r'(?<!^)(?=[A-Z])', ' ', self.teamName).title()
