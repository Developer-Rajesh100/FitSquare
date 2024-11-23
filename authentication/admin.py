from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name','last_name', 'email', 'gender', 'mobile', 'dob', 'weight', 'height', 'blood_group']

    def username(self, object):
        return object.user.first_name
    def first_name(self, object):
        return object.user.first_name
    def last_name(self, object):
        return object.user.last_name
    def email(self, object):
        return object.user.email

admin.site.register(Member, MemberAdmin)