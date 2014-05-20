Django QuerySets
================================================================

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
