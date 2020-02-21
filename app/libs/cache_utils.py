# coding: utf-8

from datetime import datetime, timedelta
import time
from functools import wraps, partial, lru_cache

def cache_it(fn=None, timeout=60): # one minute by default
    '''
    A decorator to cache a function.
    Usage:
        @cache_it(timeout=60)
        def func(x):
            return x*2
    '''
    if not fn: return partial(cache_it, timeout=timeout)
    my_cache = {}
    @wraps(fn)
    def _inner_fn(*args,**kwargs):
        kws = sorted(kwargs.items()) # in python3.6+ you dont need sorted
        key = tuple(args)+tuple(kws)
        if key not in my_cache or time.time() > my_cache[key]['expires']:
            my_cache[key] = {"value":fn(*args,**kwargs),"expires":time.time() + timeout}
        return my_cache[key]["value"]
    return _inner_fn


def timed_cache(**timedelta_kwargs):
    def _wrapper(f):
        update_delta = timedelta(**timedelta_kwargs)
        next_update = datetime.utcnow() - update_delta
        # Apply @lru_cache to f with no cache size limit
        f = lru_cache(None)(f)

        @wraps(f)
        def _wrapped(*args, **kwargs):
            nonlocal next_update
            now = datetime.utcnow()
            if now >= next_update:
                f.cache_clear()
                next_update = now + update_delta
            return f(*args, **kwargs)
        return _wrapped
    return _wrapper
