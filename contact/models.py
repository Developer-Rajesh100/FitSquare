from django.db import models
from authentication.models import Member

########## Contact Model ##########
class Contact(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    submitted_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.member.user.username}"