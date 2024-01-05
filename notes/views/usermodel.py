from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from notes.models import NotesUser
from notes.settings import FAILURE_STATUS, SUCCESS_STATUS
from notes.views import decorators
from notes.views.common import get_object_or_none
from notes.views.response import generate_response


@api_view(['POST'])
@decorators.input_validator(data_key_value=['username', 'password'])
def user_login_auth_and_token(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        hs_user = get_object_or_none(NotesUser, user=user)
        if hs_user is None:
            return Response(generate_response(FAILURE_STATUS, 'Unauthorized access!'),
                            status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        auth_data = get_tokens_for_user(request.user)
        return Response({**auth_data}, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }