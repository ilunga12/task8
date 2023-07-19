from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_student = models.BooleanField(default=False)

class studentreg(models.Model,):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name="student")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    rollnumber = models.CharField(max_length=100)
    collegename = models.CharField(max_length=100)

    def __str__(self):
        return self.name