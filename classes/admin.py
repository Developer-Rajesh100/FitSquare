from django.contrib import admin
from .models import Classes

# Register your models here.
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['image', 'online_meeting_link', 'title', 'description', 'instructor', 'duration', 'hold_on', 'difficulty_level', 'status', 'category']

admin.site.register(Classes, ClassesAdmin)