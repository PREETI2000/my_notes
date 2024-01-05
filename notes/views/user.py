from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from notes.models import NotesUser
from notes.settings import SUCCESS_STATUS
from notes.views import decorators, response


@api_view(['POST'])
@decorators.input_validator(data_key_value=['name', 'email', 'password'])
def create_user(request):
    name = request.data['name']
    email = request.data['email']
    password = request.data['password']
    user = User.objects.create(username=email,
                               email=email,
                               password=password)
    user.save()
    NotesUser.objects.create(user=user, name=name)
    return Response(response.generate_response(SUCCESS_STATUS, 'Successfully created account!'), status=status.HTTP_200_OK)
