from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views.notes import notes, search_notes
from .views.user import create_user
from .views.usermodel import user_login_auth_and_token

urlpatterns = [

    path('auth/signup', create_user, name='create_user'),
    path('api/notes', notes, name='notes'),
    path('api/search', search_notes, name='search_notes'),

    # JWT Token
    path('auth/login/', user_login_auth_and_token, name='token_obtain_pair'),
    path('auth/logout/', jwt_views.TokenBlacklistView.as_view(), name='token_blacklist'),




]