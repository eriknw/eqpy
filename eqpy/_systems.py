import itertools
import types
import sympy

from ._compatibility import range, integer_types, ellipsis_type
from ._utils import isiterable


class BaseSystem(object):
    def __init__(self, **kwargs):
        """TODO

        keyword arguments:
            prefix
            prefix_include
            prefix_exclude
            suffix
            suffix_include
            suffix_exclude
            dummies
        """
        self.prefix = kwargs.get('prefix', '')
        self.prefix_include = kwargs.get('prefix_include', [])
        self.prefix_exclude = kwargs.get('prefix_exclude', [])
        self.suffix = kwargs.get('suffix', '')
        self.suffix_include = kwargs.get('suffix_include', [])
        self.suffix_exclude = kwargs.get('suffix_exclude', [])
        self.dummies = kwargs.get('dummies', [])
        if self.dummies is False:
            self.dummies = []
        self.symbols = {}
        self.symbolnames = {}  # XXX necessary?
        self.userdict = {}
        self.equations = {}
        self.assumptions = set()
        # error if both include and exclude are defined
        if self.prefix_include and self.prefix_exclude:
            raise ValueError('"prefix_include" and "prefix_exclude" may not '
                             'both be specified')
        if self.suffix_include and self.suffix_exclude:
            raise ValueError('"suffix_include" and "suffix_exclude" may not '
                             'both be specified')

    def symbol(self, name):
        if name in self.symbols:
            return self.symbols[name]

        prefix = (
            not self.prefix_exclude and name in self.prefix_include or
            not self.prefix_include and name not in self.prefix_exclude
        ) and self.prefix or ''
        suffix = (
            not self.suffix_exclude and name in self.suffix_include or
            not self.suffix_include and name not in self.suffix_exclude
        ) and self.suffix or ''

        if isinstance(name, integer_types):
            # all integers are currently treated as dummy variables
            fullname = prefix + str(name) + suffix
            symbol = sympy.Dummy(fullname)
        else:
            fullname = prefix + name + suffix
            if self.dummies is True or name in self.dummies:
                symbol = sympy.Dummy(fullname)
            else:
                symbol = sympy.Symbol(fullname)

        self.symbols[name] = symbol
        self.symbolnames[symbol] = name  # XXX needed?
        return symbol

    def equation(self, name, expr):
        if isinstance(expr, sympy.Equality):
            self.equations[name] = [sympy.Eq(name, expr.lhs),
                                    sympy.Eq(name, expr.rhs)]
        elif isiterable(expr):
            self.equations[name] = list(sympy.Eq(name, ex) for ex in expr)
        else:
            self.equations[name] = [sympy.Eq(name, expr)]

    def assumption(self, *relations, **assumptions):
        pass


class System(object):
    def __init__(self, **kwargs):
        self.__dict__[...] = BaseSystem(**kwargs)

    def __getattr__(self, name):
        symbol = self[...].symbol(name)
        self.__dict__[name] = symbol
        return symbol

    def __setattr__(self, name, value):
        if not isinstance(name, (sympy.Symbol, sympy.Dummy)):
            name = getattr(self, name)
        self[...].equation(name, value)

    def __getitem__(self, key):
        if isinstance(key, ellipsis_type):
            return self.__dict__[...]
        elif isinstance(key, integer_types):
            return self[...].symbol(key)
        elif isinstance(key, (sympy.Symbol, sympy.Dummy)):
            return self[...].equations[key]
        elif isinstance(key, types.SliceType):
            if key.stop is None:
                raise ValueError('slice must include stop index')
            indices = range(key.start or 0, key.stop, key.step or 1)
            return tuple(self[...].symbol(index) for index in indices)
        else:
            return self[...].userdict[key]

    def __setitem__(self, key, value):
        if isinstance(key, integer_types):
            symbol = self[...].symbol(key)
            self[...].equation(symbol, value)
        elif isinstance(key, (sympy.Symbol, sympy.Dummy)):
            self[...].equation(key, value)
        elif isinstance(key, types.SliceType):
            if key.stop is None:
                raise ValueError('slice must include stop index')
            indices = range(key.start or 0, key.stop, key.step or 1)
            if len(indices) != len(value):
                raise ValueError('slice and values must have same length')
            for i, index in enumerate(indices):
                symbol = self[...].symbol(index)
                self[...].equation(symbol, value[i])
        else:
            self[...].userdict[key] = value

    def __call__(self, *relations, **assumptions):
        self[...].assumption(*relations, **assumptions)

    def __iter__(self):
        return itertools.chain.from_iterable(self[...].equations.values())

    def __contains__(self, item):
        return item in self[...].equations or item in self[...].userdict
