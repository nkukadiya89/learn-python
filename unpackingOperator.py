#When we need to access or print individual elements from the list or etc. we can use unpacking operator

numbers = [1,2,3]
print(numbers)
# [1,2,3]
#but if i need 1,2,3 individual (*)
print(*numbers)

num = list(range(5))
print(num)
print([*num, *"Hello"])
