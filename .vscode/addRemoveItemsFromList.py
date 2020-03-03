# Add or Remove items from the list

latters = ["a","b","c","d"]

#Add
latters.append("E")
latters.insert(0,"z")
print(latters)

#Remove
latters.pop(0)
print(latters)

latters.remove("c")
print(latters)

del latters[0:2]
print(latters)

latters.clear()
print(latters)
