#write a program to find the maximum of two numbers
def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b
     
# Driver code
a =int(input("Enter the no 1:")) 
b = int(input("Enter the no 2:"))
print(maximum(a, b))3