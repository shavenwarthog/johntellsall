
.. Django QuerySets and Functional Programming #2 slides file, created by
   hieroglyph-quickstart on Sat Jul 19 13:59:19 2014.


Django QuerySets and Functional Programming #2
==============================================

Contents:


for Professional Python group at TrueCar
Chris



IDEAS
=====

iterators/generators = "stream"

	- itertools

FP: easy programming with composition

	- functions

	- no side effects

QuerySet results as a stream


Iterators
=========

iterator ~ stream
-----------------


An iterator is a *stream* of data -- sort of a restricted, very
efficient list

>>> list([1,2])
[1, 2]

>>> iter([1,2])
<listiterator object at 0x7f429d83c750>

.. note::

   iterators have a item and next and that's it
   - Preferred, because they take almost no space


File iterator
----------------

iterate across a *stream* of strings

>>> f = open('ing.txt')
>>> for line in f:
    print line

>>> # Old Fashioned
1.5 oz whiskey
1 tsp water
0.5 tsp sugar
2 dash bitters
   
.. note::

   you already use iterators

   Ex: Database iterator


What can you do with a iterator?
----------------------------------------------------------------

>>> f = open('ing.txt')
>>> f.next()
'# Old Fashioned\n'
>>> f.next()
'1.5 oz whiskey\n'


What happens at the end?
----------------------------------------------------------------

>>> f = open('/dev/null')
>>> f.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

>>> iter([]).next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


List very similar to Iterator
----------------------------------------------------------------

Iterator is a *stream* of objects

.. code-block:: python

   for line in open('ing.txt'):
       print line

   for num in iter([2,4,6,8]):
       print num

   for num in [2,4,6,8]:
       print num

   for name in glob.iglob('*.txt'):
       print name


What can you *not* do with an iterator?
---------------------------------------

**no slicing**

>>> f = open('ing.txt')
>>> f[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'file' object has no attribute '__getitem__'


What can you *not* do with an iterator?
---------------------------------------

**no length**

>>> f = open('ing.txt')
>>> len(f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'file' has no len()


Common Iterator Functions
----------------------------------------------------------------

.. hlist::
* .. py:function:: enumerate(iter)
* .. py:function:: sorted(iter)
* .. py:function:: range(stop)
* .. py:function:: filter(func/None, iter)
* .. py:function:: map(func, *iterables)


List/Iterator Equivalents
-------------------------

.. py:function:: islice(iter, num)

>>> list([1,2,3])[:1]
[2]

>>> from itertools import *
>>> iter([1,2,3])[:1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'listiterator' object has no attribute '__getitem__'
>>> islice(iter([1,2,3]), 2)
<itertools.islice object at 0x7f429d7de9f0>
>>> list(islice(iter([1,2,3]), 2))
[1, 2]


iter: chain
----------------------------------------------------------------

**chain(iter*)** gives elements of each stream in order
Equivalent to **+** for lists.

>>> [1,2]+[3]
[1, 2, 3]

>>> from itertools import *
>>> chain(iter([1,2]), iter([3]))
<itertools.chain object at 0x7f429d848510>
>>> list( chain(iter([1,2]), iter([3])) )
[1, 2, 3]


.. note::

   stream of objects with state
   lazy vs eager
   ****************************************************************

iter: islice
----------------------------------------------------------------

**islice(iter, num)** -- get counted elements of stream
Equivalent to slice operator for lists.

>>> list([1,2,3])[:1]
[2]

>>> from itertools import *
>>> iter([1,2,3])[:1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'listiterator' object has no attribute '__getitem__'
>>> islice(iter([1,2,3]), 2)
<itertools.islice object at 0x7f429d7de9f0>
>>> list(islice(iter([1,2,3]), 2))
[1, 2]



Functional Programming
==============================


FP vs others
------------

procedural: list of instructions

object oriented: object has state and specific functions to
query/modify state.  Easy to specialize by subclassing

**functional: functions operate on immutable objects**

.. note::

   https://docs.python.org/dev/howto/functional.html


Practical Advantages to FP
--------------------------

   * Modularity
   * `Composability!`_
   * Ease of debugging and testing 
   * Caching
   * Parallelization
   * Buzzwordy!

.. _`Composability!`: http://en.wikipedia.org/wiki/Composability


Functional Programming example
------------------------------

Example: Windows INI-file parser; aka ConfigParser

1. stream of lines

2. stream of valid lines (no comments, has key-value)

3. stream of key-value match objects

4. dictionary

5. TBD: dict of dictionaries


Django QuerySets
================================================================

A queryset in Django represents a number of rows in the database,
optionally filtered by a query.


.. note:: models.py

          source: http://blog.etianen.com/blog/2013/06/08/django-querysets/

          QuerySets are Django's way of getting and updating data

          >>> from django.db import models
          class Meeting(models.Model):
          name = models.CharField(max_length=100)
          meet_date = models.DateTimeField()


QuerySet review
----------------------------------------------------------------
>>> m = Meeting.objects.get(id=12)
<Meeting: Meeting object>

>>> Meeting.objects.get(id=12).__dict__
{'meet_date': datetime.datetime(2014, 5, 20, 7, 0, tzinfo=<UTC>),
'_state': <django.db.models.base.ModelState object at 0x2bd1050>,
'id': 3, 'name': u'LA Django Monthly Meeting'}

>>> x = Meeting.objects.filter(name__icontains='go')
>>> for a in x: print a.name
LA Django Monthly Meeting


QuerySet and iterators
----------------------------------------------------------------

QuerySets can be shifty

>>> x = Meeting.objects.filter(name='java')
>>> x
[]
>>> type(x)
<class 'django.db.models.query.QuerySet'>


Functional QuerySets
================================================================

.. rst-class:: build

   How can you tell if a list is empty or not?

   . an iterator?

   . a QuerySet?


Empty List
==========

.. note::

   *How can you tell if a list is empty or not?*

A: Empty List
----------

>>> bool([])
False
>>> bool(['beer'])
True

.. note::
   Lists are *eager* -- always know everything


Empty Iterator
==============

.. note::
   *How can you tell if an iterator is empty or not?*


A: Empty Iterator
-----------------

>>> x=iter([1,2])
>>> bool(x)
True
>>> x=iter([])
>>> bool(x)
True

.. note::
   Iterators are *lazy* -- don't know what they contain!


How can you tell if a QuerySet is empty or not?
================================================================


QuerySet like Iterator
----------------------------------------------------------------

filter with QuerySet:

>>> from meetup.models import *
>>> Meeting.objects.filter(id=1)
[<Meeting: Meeting object>]

filter with list:

>>> filter(lambda d: d['id']==1, [{'id':1}, {'id':2}])
[{'id': 1}]

filter with iterator:

>>> list(ifilter(lambda d: d['id']==1, iter([{'id':1}, {'id':2}])))
[{'id': 1}]


Because QuerySet *is* an iterator
----------------------------------------------------------------

>>> from meetup.models import *
>>> Meeting.objects.filter(id=1)
[<Meeting: Meeting object>]

>>> type(Meeting.objects.filter(id=1))
<class 'django.db.models.query.QuerySet'>


.. note::

   similar to iter: dynamic/lazy; list(qs)

   diff: stream of objs, same class
   qs[:3] <=> islice(it, 3)
   bool(iter) vs qs.empty()

   >>> a=iter([])
   >>> bool(a)
   True

   >>> a=[] ; bool(a)
   False

   qs.count()

   laziness is explicit: prefetch_related
   
   qs.values(); qs.values_list(); qs.values-list(flat=True)


Can mix and match
----------------------------------------------------------------

>>> Meeting.objects.all()[0].id
1

>>> islice( Meeting.objects.all(), 1).next().id
1

>>> from itertools import *
>>> islice( Meeting.objects.all(), 1)
<itertools.islice object at 0x2bb9ec0>
>>> list(islice( Meeting.objects.all(), 1))
[<Meeting: Meeting object>]


But not always
--------------


*How can you tell if a QuerySet is empty or not?*

Use x.exists(), not bool(x) -- `more efficient <https://docs.djangoproject.com/en/dev/ref/models/querysets/>`_

.. note::

   Both iterators and QuerySets are *lazy*

   In functional programming, we have functions which operate on infinite-length streams.

   With QuerySets, it's assumed we have many thousands of results, but we don't want to fetch all of them at once before returning to caller.

   Database (and Django) does a query, then gives us a few items.  Once that batch is done, QuerySet will ask the database for another batch of results.

   This means that for both iterators and query sets, we can do a
   little work, then process a batch, without waiting for the entire
   list of results.


Questions?
================

.. figure:: /_static/john-bold.jpg
   :class: fill

   john@johntellsall.com



References
----------------

Can Your Programming Language Do This? by Joel Spolsky

http://www.joelonsoftware.com/items/2006/08/01.html

Wikipedia: Functional Programming

http://en.wikipedia.org/wiki/Functional_programming

Functional Programming HOWTO by Andy Kuchling

https://docs.python.org/2/howto/functional.html

Using Django querysets effectively by Dave Hall

(best blog title ever)

http://blog.etianen.com/blog/2013/06/08/django-querysets/


HISTORICAL
==========

List/Iterator Equivalents
-------------------------

* .. py:function:: ifilter(f, iter) 

.. note::

* .. py:function:: chain(*iterables)
    .. py:function:: range(start, stop[, step]) -> counter




