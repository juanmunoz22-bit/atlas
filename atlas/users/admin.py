from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from django.contrib.auth.models import User
from users.models import UserProfile

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 'user')
    list_display_links = ('pk', 'user')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    list_filter = ('created', 'modified')

    fieldsets = (
        ('Profile', {
            'fields': (('user'),),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        }),
    )

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)