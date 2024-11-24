from django.db import models
from classes.constants import DIFFICULTY_TYPE, STATUS_TYPE


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