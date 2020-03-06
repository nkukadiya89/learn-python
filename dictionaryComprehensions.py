#Dictionary Comprehensions

number = {}

for i in range(5):
    number[i] = i*2

print(number)   

values = {x:x*2 for x in range(5)}
print(values)