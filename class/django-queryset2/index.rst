
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
----------------

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


List/Iterator Equivalents
-------------------------

* .. py:function:: ifilter(f, iter) 

.. note::

* .. py:function:: chain(*iterables)
    .. py:function:: range(start, stop[, step]) -> counter



iter: chain
----------------------------------------------------------------

**chain(streams)** gives elements of each stream in order
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

**islice(stream, num)** -- get counted elements of stream
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

**functional: functions operate on streams of objects**

.. note::

   https://docs.python.org/dev/howto/functional.html


Practical Advantages to FP
==========================

   * Modularity
   * `Composability!`_
   * Ease of debugging and testing 
   * Caching
   * Parallelization

.. _`Composability!`: http://en.wikipedia.org/wiki/Composability


Functional Programming example
------------------------------

Example: Windows INI-file parser

1. stream of lines

2. stream of valid lines (no comments, has key-value)

3. stream of key-value match objects

4. dictionary

5. TBD: dict of dictionaries

