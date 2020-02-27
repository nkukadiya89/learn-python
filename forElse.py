# forelse - else part only execute when all the itration being peformed in for loop.

Successful = False

for number in range(3):
    print("Number attempted", number)
    if Successful :
        print ("second iteration")
        break
else:
    print("complate three itration")    