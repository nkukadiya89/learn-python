#List Comprehensions its better option then map and filter

items = [
    ("Product-1",10),
    ("Product-2",20),
    ("Product-3",30)
]

maplist = list(map(lambda item: item[1],items))
print(maplist)

# maplistCo = [expression for item in items ]
maplistCo = [item[1] for item in items]
print(maplistCo)

filterlist = list(filter(lambda item : item[1] > 10,items))
print(filterlist)

filterlistCo = [item for item in items if item[1] > 10]
print(filterlistCo)
