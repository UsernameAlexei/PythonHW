#Task1
def my_range(start=0, stop=None, step=1):

    if stop is None:
        stop = start
        start = 0

    if start < stop and step>0:
        while start<stop:
            yield start
            start+=step
    else:
        while start>stop and step<0:
            yield start
            start+=step

#Task2
def cached(use_cache):
    def use(func):
        cache = {}

        def a(*args, **kwargs):
            nonlocal cache

            if not cache.get(args):
                g = func(*args, **kwargs)
                cache[args] = g
                return f'caching {g}'

            elif not use_cache:
                g = func(*args, **kwargs)
                cache[args] = g
                return f'caching {g}'

            else:
                return f'from cache {cache[args]}'

        return a

    return use

