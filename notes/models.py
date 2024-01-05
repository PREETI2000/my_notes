from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class NotesUser(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notes_user'


class Note(models.Model):
    comment = models.TextField()
    added_by = models.ForeignKey(NotesUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notes_note'



