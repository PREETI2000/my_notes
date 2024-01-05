from rest_framework import serializers

from notes.models import Note, NotesUser


class NoteUserserializer(serializers.ModelSerializer):
    class Meta:
        model = NotesUser
        fields = ['name', ]


class Notesserializer(serializers.ModelSerializer):
    added_by = NoteUserserializer(read_only=True)
    class Meta:
        model = Note
        fields = ['comment', 'added_by', 'created_at']
