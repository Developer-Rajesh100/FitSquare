from django.contrib import admin
from membership.models import Membership


# Register your models here.
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'validity', 'discount']

admin.site.register(Membership, MembershipAdmin)