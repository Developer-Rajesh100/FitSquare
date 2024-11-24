from django.db import models
from authentication.models import Member
from classes.constants import DIFFICULTY_TYPE, STATUS_TYPE, RECORD_STATUS_TYPE


########## Classes Model ##########
class Classes(models.Model):
    image = models.ImageField(upload_to='classes/image')
    title = models.CharField(max_length=500)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    hold_on = models.DateTimeField()
    duration = models.DurationField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    difficulty_level = models.CharField(max_length=50, choices=DIFFICULTY_TYPE)
    online_meeting_link = models.URLField()
    status = models.CharField(max_length=20, choices=STATUS_TYPE)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title


########## ClassesRecord Model ##########
class ClassesRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=RECORD_STATUS_TYPE, default='unbooked')
    booked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.user.username}"