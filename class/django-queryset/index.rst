
.. Django QuerySets and Functional Programming slides file, created by
   hieroglyph-quickstart on Mon May 12 14:08:05 2014.

====================
Django QuerySets and Functional Programming
====================


QuerySets are Django's way of getting data.

Example: you are interested in making drinks.  As a data object, this is:

class Ingredient(Model):

class Drink(Model):

a
================

A query is a list of filters and modifiers. It's lazy -- converted to SQL when needed.

QuerySet is the result. Also lazy -- gets executed when needed, results stream from the database.

b================



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

city_set = City.objects.filter(name="Cambridge")
# The `if` statement evaluates the queryset.
if city_set:
    # We don't need the results of the queryset here, but the
    # ORM still fetched all the rows!
    print("At least one city called Cambridge still stands!")

page
================

If you only want to see if there are *any*, then use exists().  This hits the database, but it's efficient.

   tree_set = Tree.objects.filter(type="deciduous")
# The `exists()` check avoids populating the queryset cache.
if tree_set.exists():
    # No rows were fetched from the database, so we save on
    # bandwidth and memory.
    print("There are still hardwood trees in the world!")

page
================

Here's the equilvalent to qs.exists()

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

Using Django querysets effectively by Dave Hall

http://blog.etianen.com/blog/2013/06/08/django-querysets/


Other Topics
================
South
