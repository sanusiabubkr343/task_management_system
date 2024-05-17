import pytest 
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.models import User

# we need api_client fixture and mock authentication fixtures


@pytest.fixture
def api_client():
    return APIClient()



@pytest.fixture
def mocked_authentication(mocker):

    def _user(active_user=None, is_active=True):
        if active_user:
             active_user.is_active = is_active
             active_user.save()
             active_user.refresh_from_db()
        mocked_user_data = active_user
        mocker.patch.object(JWTAuthentication, "authenticate", return_value=(active_user, None))
        return mocked_user_data

    return _user
