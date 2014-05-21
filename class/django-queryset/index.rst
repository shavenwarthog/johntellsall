
.. Django QuerySets and Functional Programming slides file, created by
   hieroglyph-quickstart on Mon May 12 14:08:05 2014.

Django QuerySets and Functional Programming
==================================================


THEME
================

By using techniques from Functional Programming, we can
make simpler, more reliable and testable code, faster.

.. note::
      Functional Programming <funcprog>
      FP in Python <fp_python>
      querysets
      Patterns and Consequences <pat_conseq>
      summary
      
.. note::

   stream of objects with state
   lazy vs eager
   Heisenberg
   ****************************************************************

.. slide:: Three Programming Paradigms
   :level: 2

   .. figure:: /_static/3-hoodlums-nancy.png
   :class: fill



Why Functional Programming
================================================================

Practical Advantages to Functional Programming
----------------------------------------------------------------

   * Modularity
   * `Composability!`_
   * Ease of debugging and testing 
   * Caching
   * Parallelization

.. rst-class:: build

   - Buzzwordy!

   - Chicks dig it!

.. _`Composability!`: http://en.wikipedia.org/wiki/Composability


FP vs Procedural programming
----------------------------------------------------------------

**procedural: list of instructions**

input, output, can modify inputs

.. code-block:: python

    def upfile(inpath, outpath):
        with open(outpath, 'w') as outf:
            for line in open(inpath):
                outf.write( line.upper() )
    
    upfile('ing.txt', '/dev/stdout')
    
.. rst-class:: build

   * how can you test this?

   * run in parallel?

.. note::

  [Many] Languages are procedural: programs are lists of instructions
  that tell the computer what to do with the program’s input.


FP vs Object Orientation
----------------------------------------------------------------

procedural: list of instructions

**object oriented: Object has state and specific functions to
query/modify state.  Easy to specialize by subclassing.**

.. code-block:: python

    class Upcase(list):
        def __init__(self, inpath):
            super(Upcase,self).__init__(
                open(inpath).readlines()
                )
        def writelines(self, outpath):
            with open(outpath, 'w') as outf:
                for line in self:
                    outf.write( line.upper() )

    Upcase('ing.txt').writelines('/dev/stdout')

.. note::

   Object-oriented programs manipulate collections of objects. Objects
   have internal state and support methods that query or modify this
   internal state in some way. Smalltalk and Java are object-oriented
   languages. C++ and Python are languages that support
   object-oriented programming, but don’t force the use of
   object-oriented features. ["Object obsessive"]

    
Functional Programming
----------------------------------------------------------------

procedural: list of instructions

object oriented: object has state and specific functions to
query/modify state.  Easy to specialize by subclassing

**functional: functions operate on streams of objects**

.. note:: preferably without internal state

FP: list of functions
----------------------------------------------------------------

>>> print '\n'.join( (
    amount(hasdata)
    for hasdata in (
        line for line in open('ing.txt')
            if isdata(line)
    )
) )

.. figure:: /_static/girl-with-beads2.jpg
   :figwidth: 50%



.. note::

   read Andy Kuchling's `Functional Programming HOWTO`_

.. _`Functional Programming HOWTO`: https://docs.python.org/2.7/howto/functional.html

.. note:: 
   Functional programming decomposes a problem into a set of
   functions. Ideally, functions only take inputs and produce outputs,
   and don’t have any internal state that affects the output produced
   for a given input.

   Eliminating side effects, i.e. changes in state that do not depend
   on the function inputs, can make it much easier to understand and
   predict the behavior of a program

   http://en.wikipedia.org/wiki/Functional_programming


FP: upcase
----------------------------------------------------------------

functional: functions operate on streams of objects

.. note , preferably without internal state

.. code-block:: python

    def upcase(lines):
        for line in lines:
            yield line.upper()

    def writelines(outpath, lines):
        with open(outpath, 'w') as outf:
            for line in lines:
                outf.write( line )
 
    writelines( '/dev/stdout',
                upcase( open('ing.txt') )
                )

FP: upcase 2
----------------------------------------------------------------

.. code-block:: python

    def upcase(lines):
        # IN: stream of lines; OUT: stream of lines
        for line in lines:
            yield line.upper()

    def writelines(outpath, lines):
        # IN: stream of lines; OUT: nothing
        with open(outpath, 'w') as outf:
            for line in lines:
                outf.write( line )
 
    # open() is OUT: stream of lines
    writelines( '/dev/stdout',
                upcase( open('ing.txt') )
                )
    


.. note::
   Generally you'll mix these styles. IE: function that returns
   a stream of objects.
   ****************************************************************


Functional Programming in Python
================================================================

Old Primary Functions
----------------------------------------------------------------

.. py:function:: filter(function, iterable)

   Construct a **list** from those elements of iterable for which function returns true.

.. py:function:: map(function, iterable, ...)

   Apply function to every item of iterable and return a **list** of the results. 

>>> map(None, (1,2))
[1, 2]

.. note:: If additional iterable arguments are passed, function must
   take that many arguments and is applied to the items from
   all iterables in parallel. If one iterable is shorter than
   another it is assumed to be extended with None items. If
   function is None, the identity function is assumed; if there
   are multiple arguments, map() returns a list consisting of
   tuples containing the corresponding items from all iterables
   (a kind of transpose operation). The iterable arguments may
   be a sequence or any iterable object; the result is always a
   list.

.. py:function:: reduce(function, iterable[, initializer])

   Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.


.. note:: .. py:function:: enumerate(sequence[, start=0])

   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)


FP: important dataset
----------------------------------------------------------------

>>> print open('ing.txt')
# Old Fashioned
1.5 oz whiskey
1 tsp water
0.5 tsp sugar
2 dash bitters

Functional Prog for Better Booze!
----------------------------------------------------------------

.. figure:: /_static/bourbon-old-fashioned.jpg

FP: filter
----------------

>>> def isdata(line):
    return not line.startswith('#')

>>> print ''.join( filter(isdata, open('ing.txt')) )
1.5 oz whiskey
1 tsp water
0.5 tsp sugar
2 dash bitters

.. py:function:: filter(function, iterable)

   Construct a **list** from those elements of iterable for which function returns true.


FP: map, filter
----------------

>>> def amount(line):
    return str(line.split()[:2])
>>> def isdata(line):
    return not line.startswith('#')

>>> print '\n'.join( map(amount, filter(isdata, open('ing.txt'))) )
['1.5', 'oz']
['1', 'tsp']
['0.5', 'tsp']
['2', 'dash']

.. py:function:: map(function, iterable, ...)

   Apply function to every item of iterable and return a **list** of the results. 


Recommended: generator expressions
----------------------------------------------------------------

**filter replacement**

>>> print (line for line in open('ing.txt') if 'whiskey' in line)

**compare with**

*filter(function, iterable)*

.. note::
   high performance, memory efficient generalization of list comprehensions [1] and generators [2].
   http://legacy.python.org/dev/peps/pep-0289/


filter replacement
----------------------------------------------------------------

>>> print (line for line in open('ing.txt') if 'whiskey' in line)
<generator object <genexpr> at 0x7f429d7c8eb0>

filter replacement
----------------------------------------------------------------

>>> print list((line for line in open('ing.txt') if 'whiskey' in line)**)
['1.5 oz whiskey\n']

original FP #1
----------------------------------------------------------------
>>> def isdata(line):
    return not line.startswith('#')

>>> def amount(line):
    return str(line.split()[:2])

>>> print '\n'.join( map(amount, filter(isdata, open('ing.txt'))) )
['1.5', 'oz']
['1', 'tsp']
['0.5', 'tsp']
['2', 'dash']


updated FP #1
----------------------------------------------------------------
>>> def isdata(line):
    return not line.startswith('#')

>>> def amount(line):
    return str(line.split()[:2])

>>> print '\n'.join( (
    amount(hasdata)
    for hasdata in (
        line for line in open('ing.txt')
            if isdata(line)
    )
) )
['1.5', 'oz']
['1', 'tsp']
['0.5', 'tsp']
['2', 'dash']




Iterator Functions
----------------------------------------------------------------

.. py:function:: xrange(stop) -> counter (xrange object)
.. py:function:: xrange(start, stop[, step]) -> counter

.. py:function:: chain(*iterables)

.. py:function:: ifilter()	pred, seq	elements of seq where pred(elem) is True	ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
.. py:function:: ifilterfalse()	pred, seq	elements of seq where pred(elem) is False	ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
.. py:function:: islice()	seq, [start,] stop [, step]	elements from seq[start:stop:step]	islice('ABCDEFG', 2, None) --> C D E F G
.. py:function:: imap()	func, p, q, ...	func(p0, q0), func(p1, q1), ...	imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
.. py:function:: starmap()	func, seq	func(*seq[0]), func(*seq[1]), ...	starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
.. py:function:: tee()	it, n	it1, it2 , ... itn splits one iterator into n	 
.. py:function:: takewhile()	pred, seq	seq[0], seq[1], until pred fails	takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
.. py:function:: izip()	p, q, ...	(p[0], q[0]), (p[1], q[1]), ...	izip('ABCD', 'xy') --> Ax By
.. py:function:: izip_longest()	p, q, ...	(p[0], q[0]), (p[1], q[1]), ...	izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-




iter: chain
----------------------------------------------------------------

**chain(streams)** gives elements of each stream in order

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


Django QuerySets
================================================================

QuerySets are Django's way of getting and updating data

models.py
----------------

>>> from django.db import models

class Meeting(models.Model):
    name = models.CharField(max_length=100)
    meet_date = models.DateTimeField()

Like Iterator
----------------

>>> from meetup.models import *
>>> Meeting.objects.filter(id=1)
[<Meeting: Meeting object>]

Because it *is* an iterator
----------------------------------------------------------------

>>> from meetup.models import *
>>> Meeting.objects.filter(id=1)
[<Meeting: Meeting object>]

>>> type(Meeting.objects.filter(id=1))
<class 'django.db.models.query.QuerySet'>



A query describes what kind of data you want -- one or more Models

Commonly in Django we just specify the query then hand the results -- the QuerySet -- directly to a template for rendering

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



historical
================================================================


QuerySets are Django's way of getting data.




Example: you are interested in making drinks.  As a data object, this is:

class Ingredient(Model):

class Drink(Model):

a
================


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








Questions?
================

.. figure:: /_static/john-bold.jpg
   :class: fill

.. note::   CC BY-SA http://www.flickr.com/photos/tamburix/2900909093/


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
