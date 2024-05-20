#write a program to find the sum of digits of a given number'
n = int(input("Enter the value: "))
result = sum(int(digit) for digit in str(n))
print("The output will be: ",result)