#Dictionary in python

point = {"x":10,"y":20}
point = dict(x=30,y=45)
print(point["x"])

#access dic variables
point["x"] = 4
point["y"] = 5

print(point)

#check wether a is in dictionary or not
if "a" in point :
    print(point["a"])

#check wether a is in dictionary or not
print(point.get("a"))    

for key,val in point.items():
    print(key,val)

