from django.contrib import admin
from .models import Classes, ClassesRecord

########## Classes Admin ##########
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['id','image', 'online_meeting_link', 'title', 'description', 'instructor', 'duration', 'hold_on', 'difficulty_level', 'status', 'category']

admin.site.register(Classes, ClassesAdmin)


########## ClassesRecord Admin ##########
class ClassesRecordAdmin(admin.ModelAdmin):
    list_display = ['username', 'title', 'status', 'booked_on']

    def username(self, object):
        return object.member.user.username
    def title(self, object):
        return object.classes.title

admin.site.register(ClassesRecord, ClassesRecordAdmin)