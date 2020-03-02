# Accessing List Items by different ways

numbers = list(range(20))

#below code return value from start to end - 1
number = numbers[0:3]
print(number)

#use for every X number get from list
everysecondele = numbers[::2]
print(everysecondele)

#Reverse list
everysecondele = numbers[::-1]
print(everysecondele)


#Reverse list
reverseList = numbers[2::-1]
print(reverseList)