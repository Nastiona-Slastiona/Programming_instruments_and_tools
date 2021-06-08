from django import urls
import pytest
from django.test import Client, RequestFactory
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.auth import get_user_model
from django.urls import reverse
from memlife.memacc.models import Profile
from memlife.memacc.views import edit, user_login, dashboard,register

User = get_user_model()
profile = Profile.ojects.get(id=1)

@pytest.mark.parametrize('param', [
    ('register'),
    ('login'),
    ('dashboard'),
    ('edit'),
    ('create')
])
def test_render_login_views(client, param):
    temp_url = reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200 or resp.status_code == 302

def test_login_get_view(user_data):
        factory = RequestFactory()
        request = factory.get('')
        request.user = user_data
        response = user_login(request)
        assert response.status_code == 200

@pytest.mark.django_db
def test_login_post_view(user_data,db):
    c = Client()
    login_url = urls.reverse('login')
    response = c.post(login_url, {'username':'_user','password':'_password'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_login(user_data,db):
    client = Client()
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('login')
    user = user_model.objects.create(username='1_user', password='1_passord')
    resp = client.post(login_url,{'username':'1_user','password':'1_password'})
    assert user_model.objects.count() == 2
    assert resp.status_code == 200

def test_response_from_profile_view(user_data):
        factory = RequestFactory()
        request = factory.get('')
        request.user = user_data
        response = edit(request)
        assert response.status_code == 200

def test_response_from_registration_view():
    factory = RequestFactory()
    request = factory.get('/register/')
    request.user = profile
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)
    response = register(request)
    assert response.status_code == 200

def test_acc_manager_user_perms():
    test_user = User.objects.create_user('user1', 'user1@mail.ru', 'password1')
    assert test_user.username != 'user02'
    assert test_user.has_perm(test_user.is_admin) == False


def test_acc_manager_superuser():
    test_user = User.objects.create_superuser('user2', 'user2@mail.ru', 'password2')
    assert test_user.email == 'user2@mail.ru'
    assert test_user.has_perm(test_user.is_admin) == True