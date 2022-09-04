from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    fields = (('writed', 'publish',), 'name', 'description', 'count')

    list_display = ('name', 'description', 'count')
    list_filter = ('name', 'count')


admin.site.register(Book, BookAdmin)
