def func1(func_to_decorate):
    def new_func(*args, **kwargs):
        print "Function has been decorated.  Congratulations."
        # Do whatever else you want here
        return func_to_decorate(*args, **kwargs)
    return new_func


@func1
def print_args(*args):
    for arg in args:
        print arg


print_args(1, 2, 3)
