def foo(x):
    def too(y):
        return x * y
    return too
    
foo(3)(5)
