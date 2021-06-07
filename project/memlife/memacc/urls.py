from django.contrib.auth.views import LogoutView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView, logout_then_login, PasswordChangeDoneView,PasswordChangeView
from django.urls.conf import re_path, path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/',user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logged_out'),
    path('logout-then-login/', 
        logout_then_login,
        name='logout_then_login'),
    path('password-change/',
        PasswordChangeView.as_view(),
        name ='password_change'),
    path('password-change/done/',
        PasswordChangeDoneView.as_view(), 
        name ='password_change_done'),
    path('password-reset/',
        PasswordResetView.as_view(),  
        name ='password_reset'),
    path('password-reset/done/',
        PasswordResetDoneView.as_view(), 
            name ='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 
        PasswordResetConfirmView.as_view(), 
        name='password_reset_confirm'),
    path('password-reset/complete/', 
        PasswordResetCompleteView.as_view(), 
        name='password_reset_complete'),
    path('edit/', edit, name='edit'),
    path('register/', register, name='register'),
    path('api/', include(router.urls)),
]