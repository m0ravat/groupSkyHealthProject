from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashes password
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    Role_Choices = [
        ("Engineer", "Engineer"),
        ("teamLeader", "Team Leader"),
        ("deptLeader", "Department Leader"),
        ("seniorManager", "Senior Manager"),
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    role = models.CharField(choices=Role_Choices, max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.email
        

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


