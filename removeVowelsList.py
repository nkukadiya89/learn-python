#Remove Vowels aeiou from list

#vowels

vowels = 'aeiou'

# static list
#listData = ['a','b','c','d','e','i','o','u','x','y','z']

#Take input from user

listData = input("Enter any string which contains vowels:")

output = ''

#iterate and check for vowel in list
for i in listData:
    if i in vowels:
        continue
    else:
        output = output + i


print(output)