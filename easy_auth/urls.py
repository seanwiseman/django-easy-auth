from django.conf.urls import url
from easy_auth.views import (
    LoginAuthView,
    LogoutAuthView,
    PasswordChangeAuthView,
    PasswordChangeDoneAuthView,
    PasswordResetAuthView,
    PasswordResetConfirmAuthView,
    PasswordResetDoneAuthView,
    PasswordResetCompleteAuthView
)


urlpatterns = [
    url(r'^change_password_done', PasswordChangeDoneAuthView.as_view(), name='change_password_done'),
    url(r'^change_password', PasswordChangeAuthView.as_view(), name='change_password'),
    url(r'^login', LoginAuthView.as_view(), name='login'),
    url(r'^logout', LogoutAuthView.as_view(), name='logout'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmAuthView.as_view(),
        name='password_reset_confirm'
        ),
    url(r'^password_reset_complete', PasswordResetCompleteAuthView.as_view(), name='password_reset_complete'),
    url(r'^password_reset_done', PasswordResetDoneAuthView.as_view(), name='password_reset_done'),
    url(r'^password_reset', PasswordResetAuthView.as_view(), name='password_reset'),
]
