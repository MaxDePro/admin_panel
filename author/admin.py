from django.contrib import admin

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic')
    list_filter = ('name', 'id', 'books')


admin.site.register(Author, AuthorAdmin)
