[![Code Health](https://landscape.io/github/seanwiseman/django-easy-auth/master/landscape.svg?style=flat)](https://landscape.io/github/seanwiseman/django-easy-auth/master)

# django-easy-auth
This app allows you drop in user authentication functionality using Django's built in views.

The app gives you 8 url endpoints which handle:
- user login
- user logout
- change user password (whilst authenticated)
- reset user password via email

Requirements
------------

Django Easy Auth requires:

    python 2.7 or greater
    django 1.11 or greater
    django-crispy-forms 1.6.0 or greater

Installation
------------

Using ``pip``:

    pip install django-easy-auth

Go to https://github.com/seanwiseman/django-easy-auth if you need to download a package or clone the repo.

Setup
-----

Open ``settings.py`` and add ``easy_auth`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        'easy_auth',
    )
    
Include easy_auth urls in your project_name.urls.py file along with your other base url namespaces:
    
    import easy_auth
    
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^auth/', include('easy_auth.urls', namespace='auth')),
    ]

The templates in easy_auth/templates all extend from 'base.html', this would normally be the base html file in your project.

easy_auth/templates/login.html:
    
    line 1: {% extends 'base.html' %}

If your base file is named something different then please just rename this field in the temaplates to match your project. 

    line 1: {% extends 'some-other-base-file.html' %}
    
Usage
-----
Once installed and setup you now have access to the authentication endpoints anywhere in your app.

