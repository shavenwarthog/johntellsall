
.. Django Changes slides file, created by
   hieroglyph-quickstart on Thu Jul	 3 12:57:45 2014.


Django Changes in 1.7
================================================================

john@johntellsall.com

Contents:

.. toctree::
   :maxdepth: 2


THEME
================

XX

ME
====

   - Senior dev/server guy; Devops
   - 15 years experience with Python
   - first PyCon I went to had 40 people!


1.5 Changes
----------------

*users and permissions more flexible*

   extensible ``User`` model

   look up perms in templates:

      ``{% if 'someapp.someperm' in perms %}``

*better with JavaScript*

   ``{% verbatim %}`` template tag for JS

1.5 Changes #2
----------------

*other goodies*

   ``{% url "myview" %}``

   `QuerySet.bulk_create() <https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.bulk_create>`_ now has a batch_size 

   `django.utils.timezone <https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.timezone.localtime>`_ helps convert aware datetimes between time zones
   

.. note::

   1.5: 2/2013

   {% load url from future %} 
   {% url myview %} => {% url "myview" %}

   ? New view variable in class-based views context

   “ecosystem of pluggable components”
   https://docs.djangoproject.com/en/dev/ref/contrib/messages/#module-django.contrib.messages

   - StreamingHttpResponse: only useful for lots of data, not chat; https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.StreamingHttpResponse

   Deployment Checklist https://docs.djangoproject.com/en/dev/howto/deployment/checklist/


1.6 Changes (*latest*)
----------------------------------------------------------------

Python 3.2, 3.3 supported

simplified app/project templates

`deployment checklist <https://docs.djangoproject.com/en/dev/howto/deployment/checklist/>`_

database 
	better transactions

	`persistent connections <https://docs.djangoproject.com/en/dev/ref/databases/#caveats>`_ (disabled by default!)

.. note::

   Database-level autocommit is now turned on by default. This makes transaction handling more explicit and should improve performance. 

	?: queryset.none() is an EmptyQuerySet

	QuerySet methods `first()` and `last()`


1.6 Changes #2
----------------------------------------------------------------

perks
	``manage.py check``

	``validate_email()``

testing changes
	discovery of "test*.py" tests in any module

	`assertQuerysetEqual() <https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.TransactionTestCase.assertQuerysetEqual>`_

	assertNumQueries() 

.. note::

	discovery of "test*.py" tests in any module, rather than just in INSTALLED_APPS

    check: make sure current settings.py compatible with current
    version of Django

    1.6: 11/2013
    1.6.5: 5/2014
    1.6.6: ? (bugfixes)

    In addition, the test labels provided to ./manage.py test to
    nominate specific tests to run must now be full Python dotted paths
    (or directory paths), rather than
    applabel.TestCase.test_method_name pseudo-paths. This allows
    running tests located anywhere in your codebase, rather than only
    in INSTALLED_APPS. For more details, see Testing in Django.

	new runner: DiscoverRunner


1.7 Changes (*upcoming*)
----------------------------------------------------------------
	Python 3.4 support
	schema migrations(!!)
	app-model link broken
	better custom QuerySets (QuerySet methods from the Manager)
	‘check’ framework
	? cursor as context manager
	? custom lookups and transforms
	
perks
	``permission_required()`` now takes multiple perms
	``send_mail()`` allows HTML in addition to plaintext; accepts timeout
	runserver uses inotify
	``JsonResponse``
test
	assertNumQueries dumps out queries!
	! LiveServerTestCase, for Selenium

? update_or_create

advanced
	savepoints
	RSS/Atom syndication https://docs.djangoproject.com/en/dev/ref/contrib/syndication/#module-django.contrib.syndication

proxy model?

1.8 Changes (*upcoming*)
----------------------------------------------------------------

!

.. notes:

patterns() deprecated!

Questions?
================

.. figure:: /_static/john-bold.jpg
   :class: fill

   john@johntellsall.com


References
----------------


https://docs.djangoproject.com/en/dev/releases/
-----------------------------------------------

