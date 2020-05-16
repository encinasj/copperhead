#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    #profile Admin 
    list_display = ('pk','user')
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name', 
        'phone_number'
    )

    list_filter = ( 'user__is_active','user__is_staff','created', 'modified')
    fieldsets = (
        ('Profile',{
            'fields': (('user','picture'),),
        }),
        ('Metadata', {
            'fields': (('created','modified'),),
        })
    )
    readonly_fields = ('created','modified')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)