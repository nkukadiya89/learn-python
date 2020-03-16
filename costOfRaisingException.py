from timeit import timeit

#Cost of Raising Exceptions

data_1 = """
def calculate_xfactor(x):
    if x <= 0:
        raise ValueError("Age Can not be zero or lease than zero")
        return 10 / x
    else:
        print("executed else parth")

try:
    calculate_xfactor(-1)
except ValueError as ex:
    print(ex)
"""

print(timeit(data_1,number=1000))

data_2 = """
def calculate_xfactor2(x):
    if x <= 0:
        return None
    return 10 / x

result = calculate_xfactor2(-1)
if result == None:
   pass

"""

print(timeit(data_2,number=1000))