#Fizz Buzz Algorithm

def fizzBuzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input

data = int(input("Enter any number :"))
print(fizzBuzz(data))