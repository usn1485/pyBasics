
# Destructuring variable into multiple parameters.
def add(x,y):
    return x+y;

num=[5,8]
# '*' unpacks variablelist and assigns to each variable here. e.g x=5,y=8 
print(add(*num))

#Collecting Multiple arguments into single variable.
#the star in function argument unpacks the data and assigns to 4 invisible variables.
def multiply(*args):
    print(args)  #this creates a tuple of 
    total=1
    for arg in args:
        total=total*arg
    return total

print(multiply(4,6,8,6))


#Unpacking Key values from a dictionary



