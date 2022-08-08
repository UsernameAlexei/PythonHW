# Task1
def my_range(start=0, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if start < stop and step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop and step < 0:
            yield start
            start += step


# Task2
global CACHE
CACHE = {}


def cached(use_cache):
    def use(func):

        def a(*args, **kwargs):

            if not CACHE.get(args) or not use_cache:
                g = func(*args, **kwargs)
                CACHE[args] = g
                return g

            else:
                return CACHE[args]

        return a

    return use

