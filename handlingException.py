#Handling Exceptions

try:
    age = int(input("Enter your age:"))
except ValueError as ex:
    print(ex)
    print(type(ex))
    print("Please enter valid age!")
else:
    print("else part executed")    

