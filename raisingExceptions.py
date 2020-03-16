#Raising Exceptions

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