from django.contrib import admin
from membership.models import Membership, MembershipRecord


########## Membership Admin ##########
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'validity', 'discount']

admin.site.register(Membership, MembershipAdmin)


########## MembershipRecord Admin ##########
class MembershipRecordAdmin(admin.ModelAdmin):
    list_display = ['username', 'title', 'start_date', 'expire_date', 'is_active', 'auto_renew', 'purchase_on']

    def username(self, object):
        return object.member.user.username
    def title(self, object):
        return object.membership.title

admin.site.register(MembershipRecord, MembershipRecordAdmin)