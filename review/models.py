from django.db import models
from authentication.models import Member
from classes.models import Classes


########## Review Model ##########
class Review(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE,)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    title = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    helpful_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.member.user.username}"