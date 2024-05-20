#write a program to find the factorial of a nummber
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter the number:"))
print(fact(num))    