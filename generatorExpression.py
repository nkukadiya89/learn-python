from sys import getsizeof

# Using List
numbers  = [x * 2 for x in range(10)]
print(numbers)
print("Size :" + str(getsizeof(numbers)))

# Generator Expression when dataset is large for now i am 
# taking 20 only

Gnumbers  = (x * 2 for x in range(10))
for x in Gnumbers:
    print(x)
print("Size :" + str(getsizeof(Gnumbers)))
