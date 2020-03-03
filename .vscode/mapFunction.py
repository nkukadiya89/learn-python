# Using Map function we can achive same result of itratable in single line.

numberscomplex = [
    ("a",84),
    ("b",25),
    ("c",17)
]

#Using For loop in 4 line 
temp = []
for x in numberscomplex:
    temp.append(x[1])

print(temp)

# Using Map function in single line

x = list(map(lambda item: item[1],numberscomplex))
print(x)