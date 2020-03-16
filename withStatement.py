# Cleaning up resources using with statement 

try:
    with open("lists.py") as file :
        print("File opened")
except IOError:
    print ("Could not open file! Please close!")    
else:
    print("Execute successfully") 
