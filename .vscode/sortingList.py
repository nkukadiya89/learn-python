#Sorting a list

numbers = [77,54,28,95,12]

#sorting
numbers.sort()
print(numbers)

#reverse sorting
numbers.sort(reverse=True)
print(numbers)

#use of sorted - reverse short with reverse value true 
print(sorted(numbers,reverse = True))

#sort complex list

numberscomplex = [
    ("a",84),
    ("b",25),
    ("c",17)
]

def sort_item(item):
    return item[1]

numberscomplex.sort(key=sort_item)
print(numberscomplex)    


