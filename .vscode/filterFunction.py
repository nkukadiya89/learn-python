#Filter iterable list like we need only record with value is >= 20

numberscomplex = [
    ("a",84),
    ("b",25),
    ("c",17)
]

#Using For loop in 4 line 
temp = []
for x in numberscomplex:
    if x[1] >= 20:
        temp.append(x)

print(temp)

# Using Map function in single line

filtered = list(filter(lambda item: item[1] >= 20 , numberscomplex))
print(filtered)
