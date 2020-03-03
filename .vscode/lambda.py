#lamda Function is anonoymus single line function

numberscomplex = [
    ("a",84),
    ("b",25),
    ("c",17)
]

# we can write this sort_item function using lamda function 
# def sort_item(item):
#     return item[1]

numberscomplex.sort(key=lambda item: item[1])
print(numberscomplex)