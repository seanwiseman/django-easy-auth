from setuptools import setup
import easy_auth


setup(
    name='django-easy-auth',
    version=easy_auth.__version__,
    description="This app allows you drop in user authentication functionality using Django's built in views.",
    long_description="",
    packages=['easy_auth'],
    license='MIT',
    url='https://github.com/seanwiseman/django-easy-auth',
    maintainer='Sean Wiseman',
    maintainer_email='seanwiseman2012@gmail.com',
)

