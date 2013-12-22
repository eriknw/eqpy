import sys
import types

PY3 = sys.version_info[0] > 2

ellipsis_type = type(Ellipsis)
if PY3:
    integer_types = (int,)
    map = map
    filter = filter
    range = range
    zip = zip
else:
    integer_types = (int, long)
    range = xrange
    from itertools import imap as map
    from itertools import ifilter as filter
    from itertools import izip as zip
