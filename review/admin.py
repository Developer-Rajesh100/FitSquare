from django.contrib import admin
from review.models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['username', 'classes', 'title', 'rating', 'posted_on', 'helpful_count']

    def username(self, object):
        return object.member.user.username
    def classes(self, object):
        return object.classes.title

admin.site.register(Review, ReviewAdmin)