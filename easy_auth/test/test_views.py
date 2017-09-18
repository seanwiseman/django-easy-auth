from django.test import TestCase
from django.core.urlresolvers import reverse, resolve
from django.core import mail
from easy_auth.test.utils import create_user, resolves_to_correct_func
from easy_auth.views import (
    LoginAuthView,
)


class TestAuthViews(TestCase):
    test_un = 'testUserTemp'
    test_pw = 'somepassword1'

    def setUp(self):
        self.user = create_user(self.test_un, self.test_pw)

    def test_can_resolve_comment_create_view(self):
        resolver = resolve(reverse('auth:login'))

        self.assertEqual(resolver.namespace, 'auth', msg='url namespace incorrect')
        self.assertTrue(
            resolves_to_correct_func(resolver, LoginAuthView),
            msg='url does not resolve to correct function'
        )

    def test_can_get_login_view(self):
        response = self.client.get(reverse('auth:login'))
        self.assertEqual(response.status_code, 200, msg='Unable to get to login view')

    def test_can_login_via_view(self):
        response = self.client.post(
            reverse('auth:login'),
            data={
                'username': self.test_un,
                'password': self.test_pw,
            }
        )
        self.assertEqual(response.status_code, 302, msg='Did not redirect after login')
        self.assertEqual(self.client.session.get('_auth_user_id'), '1', msg='User not logged in')

    def test_will_fail_login_with_invalid_credentials(self):
        response = self.client.post(
            reverse('auth:login'),
            data={
                'username': 'invalid_un',
                'password': 'invalid_pw',
            }
        )
        self.assertEqual(response.status_code, 200, msg='User did not get sent back to login')
        self.assertFalse(
            self.client.session.get('_auth_user_id'),
            msg='User logged in when it should not have'
        )

    def test_can_logout(self):
        self.client.login(username=self.test_un, password=self.test_pw)
        response = self.client.get(reverse('auth:logout'))
        self.assertRedirects(response, '/auth/login')

    def test_can_request_password_change(self):
        url = reverse('auth:change_password')
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200, 'Unable to get password change view')

    def test_can_change_password(self):
        self.client.login(username=self.test_un, password=self.test_pw)
        data = {
            'old_password': self.test_pw,
            'new_password1': 'somenewpw',
            'new_password2': 'somenewpw',
        }
        url = reverse('auth:change_password')
        response = self.client.post(url, data=data)
        self.assertRedirects(response, '/auth/change_password_done')

    def test_can_request_password_reset(self):
        url = reverse('auth:password_reset')
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200, 'Unable to get password reset view')

    def test_can_reset_password(self):
        url = reverse('auth:password_reset')
        response = self.client.post(url, data={'email': self.user.email}, follow=True)
        self.assertEqual(response.status_code, 200, 'Unable to get password reset confirm view')
        self.assertRedirects(response, '/auth/password_reset_done')

        self.assertEqual(len(mail.outbox), 1, 'Email not sent')
        self.assertEqual(mail.outbox[0].subject, 'Password reset on example.com', 'Incorrect email subject')
