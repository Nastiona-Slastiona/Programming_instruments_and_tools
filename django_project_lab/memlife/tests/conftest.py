import pytest
from django.contrib.auth.models import User


@pytest.fixture
def user_data(db):
    user = User.objects.create(username="_user", password="_password")
    return user
