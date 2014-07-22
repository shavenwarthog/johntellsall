
parse1.py
----------------

.. code-block: python

    # 1. stream of lines
    import fileinput
    lines = fileinput.input() 
    print ''.join( lines )

::

    # very tasty
    [Old Fashioned]
    1:1.5 oz whiskey
    2:1 tsp water
    3:0.5 tsp sugar
    4:2 dash bitters
    
