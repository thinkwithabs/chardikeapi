
from django.contrib import admin
from accounts.models.user_model import (
    User
)
from accounts.models.profile import (
    Profile,UserPermission,BillingAddress
)

admin.site.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','customer_ID','get_permission_id']
admin.site.register(Profile,ProfileAdmin)
admin.site.register(UserPermission)
admin.site.register(BillingAddress)
