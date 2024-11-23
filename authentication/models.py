from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE

########## Member Model ##########
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_TYPE, max_length=20)
    mobile = models.CharField(max_length=12)
    dob = models.DateField()
    weight = models.IntegerField()
    height = models.IntegerField()
    blood_group = models.CharField(max_length=20)

    def __str__(self):
        return f"username: {self.user.username}"