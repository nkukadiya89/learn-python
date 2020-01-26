# Swap First and Last Element of List

a = [1,"Nirav","b",2,"Text"]

First = a.pop(0)
Last = a.pop(-1)

a.insert(0,Last)
a.append(First)

print("List :", a)