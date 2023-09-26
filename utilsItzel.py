import inspect


def DecFunName(fun):
    def wrapper():
        return fun.__name__
    return wrapper


def test():
    return print(type(inspect.currentframe().f_code.co_name))



test()
