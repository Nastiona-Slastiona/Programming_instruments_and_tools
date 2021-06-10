from django import urls
import pytest
from django.test import Client, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse
from memacc.models import Profile
from memacc.views import edit, user_login

User = get_user_model()

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
