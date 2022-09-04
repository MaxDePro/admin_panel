from django.contrib import admin

from .models import CustomUser


class AdminCustomUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role')

    list_filter = ('role', 'email', 'email')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'middle_name')
        }),
        ('password', {
            'fields': ('email', 'password')
        }),
        ('role', {
            'fields': ('role', 'is_active')
        }),
    )


admin.site.register(CustomUser, AdminCustomUser)

