# We can define variable in the function of out side of the function in any python file.
# Varaible which is defined in the top of file is accessible in whole file part. like in function , class.
# variable defined in function is teated as local variable and only accessible in side that function only.

# Example


a = 5

def add(a):
    a = 10
    print(a*a)

add(5) 
add(7)
print(a)