#looping over List

numbers = ["a","b","c","d"]

# by default it returns the tuple with (index , value)
# we have enumerate function which allows us to access index and value like below

for index, number in enumerate(numbers):
    print(index, number)