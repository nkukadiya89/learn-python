# When we need to pass keyword argument (like  id=1,name='abc',age=23) in variable amount of count in function then we can use this xxargs concept of python.
# By this way we can easily access the data by [key] as example below

def xxargs(**args):
    print(args['id'])
    print(args['name'])
    print(args['age'])


xxargs(id=1,name="john",age="30")    
