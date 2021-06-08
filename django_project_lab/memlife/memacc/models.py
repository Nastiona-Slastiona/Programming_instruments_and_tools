from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from mainboard.models import Mem

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
