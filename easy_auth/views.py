from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView
)


class LoginAuthView(LoginView):
    template_name = 'login.html'


class LogoutAuthView(LogoutView):
    pass


class PasswordChangeAuthView(PasswordChangeView):
    template_name = 'password_change_form.html'

    @staticmethod
    def get_success_url():
        return reverse('auth:change_password_done')


class PasswordChangeDoneAuthView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'


class PasswordResetAuthView(PasswordResetView):
    email_template_name = 'password_reset_email.html'
    template_name = 'password_reset_form.html'
    success_url = reverse_lazy('auth:password_reset_done')


class PasswordResetDoneAuthView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class PasswordResetConfirmAuthView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('auth:password_reset_complete')


class PasswordResetCompleteAuthView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

