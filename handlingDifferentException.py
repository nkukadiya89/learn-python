#Handling Different Exceptions

try:
    age = int(input("Enter your Age :"))
    div = 10 / age 
except ValueError as ex:
    print("Please enter valid age")
except ZeroDivisionError:
    print ("value not divisible by zero")    
else:
    print("Execute successfully")    