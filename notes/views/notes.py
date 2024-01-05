from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from notes.models import Note
from notes.serializers import Notesserializer
from notes.settings import SUCCESS_STATUS, FAILURE_STATUS
from notes.views import decorators, response


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@decorators.is_user_login_required()
def notes(request, notes_user):
    if request.method == 'GET':
        data = None
        note_id = request.GET.get('id')
        if note_id:
            note = Note.objects.filter(id=id)
            if note:
                data = Notesserializer(note).data
            else:
                return Response(response.generate_response(FAILURE_STATUS, 'id missing!'), status=status.HTTP_200_OK)
        else:
            notes = Note.objects.all()
            data = Notesserializer(notes, many=True).data
        return Response(response.generate_response(SUCCESS_STATUS, 'Success!',data), status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        note_id = request.GET.get('id')
        if note_id:
            Note.objects.filter(id=note_id).update(comment=request.data['note_comment'])
            return Response(response.generate_response(SUCCESS_STATUS, 'Success!',), status=status.HTTP_200_OK)
        else:
            return Response(response.generate_response(SUCCESS_STATUS, 'id missing!'), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        comment = request.GET.get('comment')
        Note.objects.create(comment=comment,added_by=notes_user)
        return Response(response.generate_response(SUCCESS_STATUS, 'Success!', ), status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        note_id = request.GET.get('id')
        Note.objects.get(id=note_id).delete()
        return Response(response.generate_response(SUCCESS_STATUS, 'Success!',), status=status.HTTP_200_OK)


@api_view(['GET'])
@decorators.is_user_login_required()
def search_notes(request, notes_user):
    all_notes = Note.objects.all()
    query = request.GET.get('q_query')
    notes = all_notes.filter(comment__contains=query)
    data = Notesserializer(notes, many=True).data
    return Response(response.generate_response(SUCCESS_STATUS, 'Success!', data), status=status.HTTP_200_OK)
