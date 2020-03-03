#Finding Items in List

latters = ["a","b","c","d"]

#return index of item
print(latters.index("d"))

#if item is in list or not then

if "E" in latters:
    print(latters.index("E"))
else:    
    print("E not found")    

#Using count method

print(latters.count("d"))    