from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at', 'end_at')
    list_filter = ('user', 'end_at')

    fieldsets = (
        ('Book', {
            'fields': ('book', 'user')
        }),
        ('Date to back book', {
            'fields': ('end_at', 'plated_end_at')
        })
    )


admin.site.register(Order, OrderAdmin)
