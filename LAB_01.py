#1) Write a python program to display the current date and time
import datetime
current = datetime.datetime.now()
print("Current date and time :",current)

# 2) Write a python program that accepts the users first and last name and prints them in reverse
f_name = input("Enter first name:")
l_name = input("Enter last name :")
rev_first = f_name[::-1]
rev_last = l_name[::-1]
print("Reversed name :",rev_first,rev_last)

# 3) Write a program that accepts n as integer (n) and computes the value of n+nn+nnn
n=int(input("Enter a number:"))
nn = int(str(n)+str(n))
nnn = int(str(n)+str(n)+str(n))
result = n+nn+nnn
print("result:",result)

# 4) Write a python program to calculate the sum of three given numbers .If the values are equal
num1 = int(input("Enter number :"))
num2 =int(input("Enter number :"))
num3 = int(input("Enter number :"))
res = num1+num2+num3

if(num1 == num2 ==num3):
    res = 3 * res
print("Sum :",res)

# 5)Write a python program to solve (x+y) * (x+y)
x = int(input("Enter number :"))
y = int(input("enter number :"))
result = (x+y)**2
print("Result :",result)

# 6) Write a python program to compute the future value of a specified principal amount,rate of interest and number of years
p = float(input("enter principal amount :"))
t = int(input("Enter years :"))
r = float(input("Enter rate of interest :"))
amount = p * (1+r/100)**t
print("Future value :",round(amount,2))
# 7) Write a program to parse to float and integer value from a string
str = input("Enter string :")
try :
    num = int(str)
    print("The input is an integer:", num)
except ValueError:
    print("The input is not an integer")
# 8) Write a python program to sum the first n positive integers
n = int(input("Enter n:"))
sum = n * (n+1) //2
print("Sum",sum)
# 9) Write a python program to calculate the sum of digits of a number
num = int(input("enter number :"))
sum =0
while(num !=0):
    res = num % 10
    sum = sum+res
    num = num//10
print("Sum of the digits:",sum)
# 10) Write a python program to get the ASCII value of a character
char = input("Enter a character :")
print("ASCII value :",ord(char))
# 11)Write a python program to check whether a string is numeric or not
str = input("enter string :")
if str.isnumeric():
    print("The input is a number:", str)
else :
    print("The input is not a number:", str)
# 12) Print a rectangle pattern with 5 rows and 3 columns of stars
for i in range(5):
    for j in range(3):
        print(" * ",end="") 
    print()
# 13) Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 
for i in range(2000,3201):
    if (i%7==0 and i%5!=0):
        print(i,end=",")
# 14) Write a program that calculates and prints the value according to the given formula Q = Square root of [(2 * C * D)/H]
import math
C = 50
H = 30
D = int(input("Enter D :"))
num = D.split(",")
result = []
for i in num:
    res = math.sqrt(2 * C * int(i) / H)
    result.append(str(int(res)))

print(",".join(result))
# 15) Write a program to print a right angle triangle with alphabets 
rows =5
alphabet = 65
for i in range(rows,0,-1):
    for j in range(i):
        print(chr(alphabet),end="")
    print()
    alphabet +=1
    