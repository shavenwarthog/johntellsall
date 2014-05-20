
.. Django QuerySets and Functional Programming slides file, created by
   hieroglyph-quickstart on Mon May 12 14:08:05 2014.

Django QuerySets and Functional Programming
==================================================


THEME
----------------

By using techniques from Functional Programming, we can
make simpler, more reliable and testable code, faster.

Contents
----------------
   .. toctree::
      Functional Programming <funcprog>
      FP in Python <fp_python>
      querysets
      Patterns and Consequences <pat_conseq>
      summary
      
.. note::

   stream of objects with state
   lazy vs eager
   Heisenberg


historical
================================================================


QuerySets are Django's way of getting data.




Example: you are interested in making drinks.  As a data object, this is:

class Ingredient(Model):

class Drink(Model):

a
================

A query describes what kind of data you want

one or more Models

commonly in Django we just specify the query then hand the results -- the QuerySet -- directly to a template for rendering

A query is a list of filters and modifiers. It's lazy -- converted to SQL when needed. Sometimes a single result is all that's needed

>>> m = Meeting.objects.get(id=12)
<Meeting: Meeting object>


More commonly, you're looking for a list of objects matching some criteria.  A QuerySet is the result. Like the query, a QuerySet is also lazy -- it gets executed when needed, and results stream from the database.

>>> x = Meeting.objects.filter(name__contains='go')
>>> Meeting.objects.all()
[<Meeting: Meeting object>]
>>> type( Meeting.objects.all() )
<class 'django.db.models.query.QuerySet'>

Note that the QuerySet doesn't hit the database unless it needs to.  Even if there are no matches, it'll return an object.

>>> type(Meeting.objects.filter(name='java'))
<class 'django.db.models.query.QuerySet'>

To see if there are any matches, convert the results into a list

>>> list(qs)
[]

This isn't efficient -- Python has to hit the database, do a search, parse each row into a separate Model object, and allocate the space for everything.  And then you just check if it's empty or not!

More efficient: ask the database if there are any matches


A *generator* is a stream of data.  QuerySets are similar -- a stream of Model objects

Since it's a stream, one you consume it, it's gone.  Printing is consuming -- thus debugging things with streams can be... interesting.

TODO: fileinput example
TODO: map/reduce
TODO: Twitter stream example?




generators
QuerySet (+ query)

State
- none*: random()
- init: open()
- other: trans = db().requestmany()



enumerate(iter) 

Iterators can be tricky to work with

- first three elements of a list:

>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(100)[:3]
[0, 1, 2]

- first three elements of iterator -- can't use slice operator!

>>> xrange(100)[:3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence index must be integer, not 'slice'

- first three elements of iterator -- use islice

>>> from itertools import *

# ... to get another iterator!

>>> islice(count(10), 3)
<itertools.islice object at 0x7f9bc54a5d08>

# turn it into a concrete list

>>> list(islice(count(10), 3))
[10, 11, 12]


>>> f=open('ing.txt')
>>> f
<open file 'ing.txt', mode 'r' at 0x7f9bc54fe4b0>

>>> f[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'file' object has no attribute '__getitem__'

>>> islice(f,1)
<itertools.islice object at 0x7f9bc54a5d60>
>>> list(islice(f,1))
['whiskey\n']
>>> list(islice(f,1))
['syrup\n']

>>> f.next()
'bitters\n'





page
================



Internally, queries are compiled into SQL, but aren't executed until needed

TODO: clarify; queries are dynamic too

qs = Event.objects.filter(pk=3) ; print qs.query

SELECT `event_event`.`id` ...
FROM `event_event`
WHERE `event_event`.`id` = 3 

page
================

q = Event.objects.filter(pk=3).values_list('id') ; print x.query
SELECT `event_event`.`id` FROM `event_event` WHERE `event_event`.`id` = 3 

>>> print q
[(3L,)]

page
================

Set operations on QuerySets

.. figure:: /_static/venn.png
   :class: fill

page
================

>>> q = Event.objects.filter(pk=3) & Event.objects.filter(name__contains='beer')
>>> print q.query
SELECT `event_event`.`id`, ...
FROM `event_event`
WHERE (`event_event`.`id` = 3  AND `event_event`.`name` LIKE BINARY %beer% )

page
================

>>> q = Event.objects.filter(pk=3) | Event.objects.filter(name__icontains='beer') ; print q.query
SELECT `event_event`.`id`, ...
FROM `event_event`
WHERE (`event_event`.`id` = 3  OR `event_event`.`name` LIKE %beer% )

page
================

An 'if' will evaluate the query, retrieving all the rows, all the fields

>>> city_set = City.objects.filter(name="Cambridge")
# The `if` statement evaluates the queryset.
if city_set:
    # We don't need the results of the queryset here, but the
    # ORM still fetched all the rows!
    print("At least one city called Cambridge still stands!")

page
================

If you only want to see if there are *any*, then use exists().  This hits the database, but it's efficient.

>>> tree_set = Tree.objects.filter(type="deciduous")
# The `exists()` check avoids populating the queryset cache.
if tree_set.exists():
    # No rows were fetched from the database, so we save on
    # bandwidth and memory.
    print("There are still hardwood trees in the world!")

page
================

Here's the equivalent to qs.exists()

qs = Event.objects.filter(pk=3); qs.query.set_limits(high=1); print qs.query 

SELECT `event_event`.`id`
FROM `event_event`
WHERE `event_event`.`id` = 3
LIMIT 1

page
================

You can add modifiers 

>>> qs = Event.objects.filter(pk=3)
>>> print qs.query
SELECT `event_event`.`id` FROM `event_event` WHERE `event_event`.`id` = 3 
>>> qs = qs.filter(pk=2)
>>> print qs.query
SELECT `event_event`.`id` FROM `event_event` WHERE (`event_event`.`id` = 3  AND `event_event`.`id` = 2 )


TBD: other databases -- Mongo? flat file?



Contents:

.. toctree::
   :maxdepth: 2


First Slide
===========

Some content on the first slide.

Second Slide
============

* A
* Bulleted
* List


Show Bullets Incrementally
==========================

.. rst-class:: build

- Adding the ``build`` class to a container
- To incrementally show its contents
- Remember that *Sphinx* maps the basic ``class`` directive to
  ``rst-class``


Questions?
================

.. figure:: /_static/john-bold.jpg
   :class: fill

   CC BY-SA http://www.flickr.com/photos/tamburix/2900909093/


References
================

Can Your Programming Language Do This? by Joel Spolsky

http://www.joelonsoftware.com/items/2006/08/01.html

Wikipedia: Functional Programming

http://en.wikipedia.org/wiki/Functional_programming

Functional Programming HOWTO by Andy Kuchling

https://docs.python.org/2/howto/functional.html

Using Django querysets effectively by Dave Hall

http://blog.etianen.com/blog/2013/06/08/django-querysets/


Other Topics
================
South
