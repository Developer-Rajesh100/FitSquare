from django.db import models
from authentication.models import Member

# Create your models here.
class Contact(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return f"{self.member.user.username}"