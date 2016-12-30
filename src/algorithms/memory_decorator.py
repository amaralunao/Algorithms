from memory_profiler import profile


def profiles(func):
    def inner(*args, **kwargs):
        if kwargs.get('_memory', False):
            wrapper = profile(func)
            del kwargs['_memory']
            return wrapper(*args, **kwargs)
        else:
            return func(*args)
    return inner
