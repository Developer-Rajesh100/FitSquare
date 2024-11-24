from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['username', 'subject', 'email', 'phone_number', 'submitted_on']

    def username(self, object):
        return object.member.user.username

