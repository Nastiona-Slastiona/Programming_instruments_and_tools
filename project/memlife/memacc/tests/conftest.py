import pytest
from django.contrib.auth import get_user_model
from memacc.models import Profile

User = get_user_model()

@pytest.fixture
def user_data(db):
    user = User.objects.create(username="_user", password="_password")
    return user

# @pytest.fixture
# def profile(db,user):
#     profile = Profile.objects.create(user=user)
#     return profile