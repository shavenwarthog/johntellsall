FP vs Procedural programming
================================================================

procedural: list of instructions

input, output, can modify inputs

.. code-block:: python

    def upfile(inpath, outpath):
        with open(outpath, 'w') as outf:
            for line in open(inpath):
                outf.write( line.upper() )
    
    upfile('ing.txt', '/dev/stdout')
    

.. note::

  [Many] Languages are procedural: programs are lists of instructions
  that tell the computer what to do with the program’s input.


FP vs Object Orientation
================================================================

object oriented: Object has state and specific functions to
query/modify state.  Easy to specialize by subclassing.

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
================================================================

F

.. note:: 
   Functional programming decomposes a problem into a set of
   functions. Ideally, functions only take inputs and produce outputs,
   and don’t have any internal state that affects the output produced
   for a given input.


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
    

FP in Practice
================================================================

practical advantages to the functional style:

* Modularity
* Composability
* Ease of debugging and testing 
* Caching
* Parallelization

.. note::
   Generally you'll mix these styles. IE: function that returns
   a stream of objects.
  

