# To make code more readable when there is multiple arguments needs to pass and not able to identity which arg is for what we can use keyword argument concept

def add(value,by):
    return value + by

print(add(10,by=15))    