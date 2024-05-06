from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    ph_no = models.CharField(max_length=20)
    dob = models.DateField()

    def __str__(self) -> str:
        return self.user.first_name + ' ' + self.user.last_name