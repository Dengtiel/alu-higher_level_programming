# Python - Test-driven development

## 0-add_integer.py


This module contains a function `add_integer(a, b)` that adds two integers (or floats, which are cast to integers). If either `a` or `b` are not integers or floats, a `TypeError` will be raised.


### Usage:
```bash
>>> from 0-add_integer import add_integer
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
98
