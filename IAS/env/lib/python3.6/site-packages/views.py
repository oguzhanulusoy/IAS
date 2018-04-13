# -*- coding: utf-8 -*-
"""
Copyright (C) Koos Zevenhoven. 

See LICENSE.txt at http://github.com/k7hoven/views for license information.

@author: Koos Zevenhoven
"""

__all__ = ['gen', 'seq']

def make(callable):
    return callable()
        
@make
class gen:
    """Generator comprehension syntax.

    Example:

    >>> list(gen[::range(3), 3, 4, ::range(5,7), 7])
    [0, 1, 2, 3, 4, 5, 6, 7]

    """

    def __getitem__(self, args):
        if not isinstance(args, tuple):
            args = args,

        @tuple
        @make
        def parts():
            part = []
            for obj in args:
                if isinstance(obj, slice):
                    if obj.start is None and obj.stop is None:
                        obj = obj.step
                        objtype = type(obj)
                        if hasattr(objtype, '__iter__'):
                            obj = iter(obj)
                        if not hasattr(type(obj), '__next__'):
                            raise TypeError(
                                f"'{objtype.__name__}' object is not "
                                "iterable and cannot be chained"
                            )
                        if part:
                            yield part
                            part = []
                        yield obj
                    else:
                        raise SyntaxError(
                            'invalid syntax in generator comprehension'
                        )
                else:
                    part.append(obj)
            if part:
                yield part

        return self.chain(*parts)
    
    @staticmethod
    def chain(*parts):
        for part in parts:
            yield from part
    chain.__qualname__ = '<views.gen>'


class LengthChangedError(RuntimeError):
    pass

def issequence(obj):
    otype = type(obj)
    return hasattr(otype, '__getitem__') and hasattr(otype, '__len__')

class Repr(str):
    def __repr__(self):
        return self

class SeqMixin:
    REPR_ITEMS = 10
    REPR_SPLIT = 5, 4
    def __repr__(self):
        template = f"<sequence view {len(self)}:" " {} >"
        if len(self) <= self.REPR_ITEMS:
            return template.format(repr([*self]))
        return template.format(
            repr([*self[:self.REPR_SPLIT[0]],
                  Repr("..."),
                  *self[-self.REPR_SPLIT[1]:]])
        )

class Seq(SeqMixin):
    def __init__(self, seq, start=None, stop=None, step=None):
        if not issequence(seq):
            raise TypeError(
                f"'{type(seq).__name__}' object is not a sequence"
            )
        self._seq = seq
        self._len_orig = len(seq)
        self._slice = slice(*slice(start, stop, step).indices(len(seq)))
        self._len = len(range(self._len_orig)[self._slice])

    @property
    def deps(self):
        return self._seq,

    def __len__(self):
        return self._len

    def __getitem__(self, subscript):
        if isinstance(subscript, tuple):
            raise TypeError("multi-indices not supperted")

        if len(self._seq) != self._len_orig:
            raise LengthChangedError(
                "length of underlying sequence has changed"
            )

        if isinstance(subscript, slice):
            idx = subscript.indices(len(self))
            start = self._slice.start + idx[0] * self._slice.step
            stop = start + self._slice.step * (idx[1] - idx[0])
            step = self._slice.step * idx[2]
            return SeqView(self._seq, start, stop, step)

        try:
            subscript.__index__
        except AttributeError:
            raise TypeError(
                "index must be an integer, a slice or have an __index__ method"
            ) from None
            
        subscript = subscript.__index__()
        if subscript < 0:
            subscript = self._len + subscript
        if subscript < 0 or subscript >= self._len:
            raise IndexError("index out of range")

        return self._seq[self._slice.start + subscript * self._slice.step]


class SeqChain(SeqMixin):
    def __init__(self, *parts):
        _len = 0
        for p in parts:
            if not issequence(p):
                raise TypeError(
                    f"'{type(p).__name__}' object is not a sequence"
                )
            _len += len(p)
        self._parts = parts
        self._len = _len

    @property
    def deps(self):
        return self._parts
    
    def __len__(self):
        return self._len

    def _find_position(self, index):
        start = 0
        if index < 0 or index >= self._len:
            return None
        for i, p in enumerate(self._parts):
            newstart = start + len(p)
            if start <= index < newstart:
                ret = (i, index - start)
            start = newstart
        if not start == self._len:
            raise LengthChangedError(
                "length of one of chained sequences has changed"
            )
        return ret
        
    def __getitem__(self, subscript):
        if isinstance(subscript, tuple):
            raise TypeError("multi-indices not supperted")
        
        if isinstance(subscript, slice):
            # Memory use could be optimized further by making a smarter
            # slice which does not hold references to unused parts
            return Seq(self, subscript.start, subscript.stop, subscript.step)
    
        try:
            subscript.__index__
        except AttributeError:
            raise TypeError(
                "index must be an integer, a slice or have an __index__ method"
            ) from None
        
        pos = self._find_position(subscript.__index__())
        if pos is None:
            raise IndexError("sequence index out of bounds")
        return self._parts[pos[0]][pos[1]]
        

@make
class seq:
    """Sequence view comprehension syntax.

    Resulting objects support slicing and indexing.

    Examples:

    >>> seq[::range(3), None, ::"abc", "Hi!"]
    <sequence view 8: [0, 1, 2, None, 'a', 'b', 'c', 'Hi!'] >

    >>> seq[::range(100)]
    <sequence view 100: [0, 1, 2, 3, 4, ..., 96, 97, 98, 99] >

    """

    def __getitem__(self, args):
        if not isinstance(args, tuple):
            args = args,
        
        @tuple
        @make
        def parts():
            part = []
            for obj in args:
                if isinstance(obj, slice):
                    if obj.start is None and obj.stop is None:
                        obj = obj.step
                        if not issequence(obj):
                            raise TypeError(
                                f"'{type(obj).__name__}' object is not "
                                "a sequence and cannot be chained"
                            )
                        if part:
                            yield part
                            part = []
                        yield obj
                    else:
                        raise SyntaxError(
                            'Invalid syntax in chain generator expression'
                        )
                else:
                    part.append(obj)
            if part:
                yield part

        return SeqChain(*parts)

    chain = staticmethod(SeqChain)
