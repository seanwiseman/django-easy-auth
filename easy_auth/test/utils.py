from django.contrib.auth.models import User


test_un = 'testUserTemp'
test_pw = 'somepassword1'


def create_user(un='', pw='', email='test@test.com') -> User:
    user = User.objects.create(username=un, password=pw, email=email)
    user.set_password(pw)
    return user.save()


def resolves_to_correct_func(resolver, expected_func) -> bool:
    return resolver.func.__name__ == expected_func.as_view().__name__
