from django.contrib import admin

# Register your models here.
from notes.models import NotesUser


class NotesUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(NotesUser, NotesUserAdmin)
