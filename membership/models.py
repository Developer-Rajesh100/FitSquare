from django.db import models
from authentication.models import Member

########## Membership Model ##########
class Membership(models.Model):
    image = models.ImageField(upload_to='membership/image')
    title = models.CharField(max_length=500)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    validity = models.PositiveSmallIntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title


########## MembershipRecord Model ##########
class MembershipRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    start_date = models.DateField()
    expire_date = models.DateField()
    is_active = models.BooleanField(default=False)
    auto_renew = models.BooleanField(default=False)
    purchase_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.user.username} {self.membership.title}"