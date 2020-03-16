#Cleaning up resources using Finally Blog

try:
    file = open("lists.py")
    age = int(input("Enter your Age :"))
    div = 10 / age 
except (ValueError,ZeroDivisionError):
    print("Please enter valid age")
else:
    print("Execute successfully") 
finally:
    print("Finally class called")
    file.close()
