
.. Django Changes slides file, created by
   hieroglyph-quickstart on Thu Jul  3 12:57:45 2014.


Django Changes
==============

Contents:

.. toctree::
   :maxdepth: 2


1.5 Changes
----------------
   1.5: 2/2013
   - extensible User model
   - {% url "myview" %}
   - {% verbatim %} template tag for JS
   ? New view variable in class-based views context
   - https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.timezone.localtime
   - QuerySet.bulk_create() now has a batch_size 
   - look up perms in templates: {% if 'someapp.someperm' in perms %} 

..
   notes
   “ecosystem of pluggable components”
   https://docs.djangoproject.com/en/dev/ref/contrib/messages/#module-django.contrib.messages

   - StreamingHttpResponse: only useful for lots of data, not chat; not recommended https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.StreamingHttpResponse

   Deployment Checklist https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

   1.5: 2/2013
   - extensible User model
   - {% url "myview" %}
   - {% verbatim %} template tag for JS
   ? New view variable in class-based views context
   - https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.timezone.localtime
   - QuerySet.bulk_create() now has a batch_size 
   - look up perms in templates: {% if 'someapp.someperm' in perms %} 

   1.6: 11/2013
   - Python 3.2, 3.3 supported
   - simplified app/project templates
   - db: better transactions; persistent connections (disabled by default!)
   - discovery of tests in any module
   - “manage.py check”
   - test: (assertQuerysetEqual)
   - deployment checklist: https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
   - QuerySet methods first() and last() 
   - test: assertNumQueries() 
   - test: new runner: DiscoverRunner
   - ?: queryset.none()
   - validate_email() 

   1.6.5: 5/2014

   1.7: upcoming
   - Python 3.4 support
   - schema migrations
   - app-model link broken
   - better custom QuerySets (QuerySet methods from the Manager)
   - ‘check’ framework
   - ? cursor as context manager
   - ? custom lookups and transforms
   - permission_required() now takes multiple perms
   - send_mail() allows HTML in addition to plaintext; accepts timeout
   - runserver uses inotify
   - JsonResponse
   - test: assertNumQueries dumps out queries!
   - ? update_or_create
   advanced
   - savepoints
   - RSS/Atom syndication https://docs.djangoproject.com/en/dev/ref/contrib/syndication/#module-django.contrib.syndication
   - proxy model?
   - ! LiveServerTestCase, for Selenium
