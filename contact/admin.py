from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['username', 'subject', 'message']

    def username(self, object):
        return object.member.user.username

admin.site.register(Contact, ContactAdmin)