from django.db import models
from authentication.models import Member

# Create your models here.
class Membership(models.Model):
    image = models.ImageField(upload_to='membership/image')
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    validity = models.PositiveSmallIntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title