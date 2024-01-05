from rest_framework.response import Response
from rest_framework import status

from notes.models import NotesUser
from notes.settings import FAILURE_STATUS
from notes.views.common import get_object_or_none
from notes.views.response import generate_response


def is_user_login_required():
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if request.user.is_authenticated:
                notes_user = get_object_or_none(NotesUser, user=request.user)
                if notes_user is None:
                    return Response(generate_response(FAILURE_STATUS, 'Unauthorized access!'),
                                    status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(generate_response(FAILURE_STATUS, 'Unauthorized access!'),
                                status.HTTP_401_UNAUTHORIZED)
            # adding appraisal_user in return from decorator
            kwargs['notes_user'] = notes_user
            return func(request, *args, **kwargs)
        return wrap
    return decorator


def input_validator(data_keys_only=None, query_params_keys_only=None, data_key_value=None, query_params_key_value=None):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if data_keys_only:
                for key in data_keys_only:
                    if key not in request.data:
                        return Response(generate_response(FAILURE_STATUS, 'Data key missing', {'Missing Key': key}),
                                    status.HTTP_400_BAD_REQUEST)
            if query_params_keys_only:
                for key in query_params_keys_only:
                    if key not in request.query_params:
                        return Response(generate_response(FAILURE_STATUS, 'Query Params key missing', {'Missing Key': key}),
                                        status.HTTP_400_BAD_REQUEST)
            if data_key_value:
                for key in data_key_value:
                    if key in request.data and not request.data[key]:
                        return Response(generate_response(FAILURE_STATUS, 'Value missing', {'Missing Value for key': key}),
                                        status.HTTP_400_BAD_REQUEST)
                    elif key not in request.data:
                        return Response(generate_response(FAILURE_STATUS, 'Data key missing', {'Missing Key': key}),
                                        status.HTTP_400_BAD_REQUEST)
            if query_params_key_value:
                for key in query_params_key_value:
                    if key in request.GET and not request.GET[key]:
                        return Response(generate_response(FAILURE_STATUS, 'Value missing', {'Missing Value for key': key}),
                                        status.HTTP_400_BAD_REQUEST)
                    elif key not in request.query_params:
                        return Response(generate_response(FAILURE_STATUS, 'Query Params key missing', {'Missing Key': key}),
                                        status.HTTP_400_BAD_REQUEST)
            return func(request, *args, **kwargs)
        return wrap
    return decorator
