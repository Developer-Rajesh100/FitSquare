from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE

########## Member Model ##########
class Member(models.Model):
    profile_picture = models.ImageField(upload_to='authentication/profile_pictures', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_TYPE, max_length=20)
    mobile = models.CharField(max_length=12)
    emergency_contact = models.CharField(max_length=12, null=True, blank=True)
    dob = models.DateField()
    weight = models.IntegerField()
    height = models.IntegerField()
    blood_group = models.CharField(max_length=20)
    join_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"