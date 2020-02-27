# Sometimes we need to pass variable number of arguments in function call so in that situation if the function has fixed 2 or 3 argument written in function definition then it will not work as expected.
# The solution of that we have barges concept in python lets check example below.


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2,2,2,2,2,2,2,2,2))