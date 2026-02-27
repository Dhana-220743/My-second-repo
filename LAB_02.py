''' 1) Write a program to create a class for student data(Student iD,name,marks,and percentage)
    Implement a method to calculate the percentage and grade(A,B,C,D) based on the percentage
    Take the values as input at runtime '''
class student :
    def __init__(self,sid,name,marks):
        self.sid=sid
        self.name=name
        self.marks=marks
    def calculate(self):
        self.percentage = sum(self.marks)/len(self.marks)
        if self.percentage >= 90:
            self.grade = 'A'
        elif self.percentage >= 80:
            self.grade = 'B'
        elif self.percentage >= 70:
            self.grade = 'C'
        else :
            self.grade = 'D'
    def display(self):
        print("Student ID : ",self.sid)
        print("Student Name :",self.name)
        print("Percentage :",self.percentage)
        print("Grade : ",self.grade)
s1 = student(1,'Santosh',[85,90,92])
s2 = student(2,'Nakamoto',[75,80,78])
s1.calculate()
s1.display()
s1.calculate()
s1.display()

''' 2) Write a program to demonstrate parametrized constructors for employee data (employeeID,name,salary,date of joining)
    Implement a method to display employee details
    '''
class Employee:
    def __init__(self,emp_id,name,salary,date_of_join):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
        self.date_of_join=date_of_join
    def display(self):
        print("\nEmployee Details")
        print("Employee ID :",self.emp_id)
        print("Employee name:",self.name)
        print("Employee salary :",self.salary)
        print("Date of joining :",self.date_of_join)
e1 = Employee("E01" , "Raju",40000, "12-31-2008")
e1.display()

''' 3) Write a program to count the number of objects created for a class and display the total
 count whenever an object is created'''
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
        print("\nTotal no of objects created:", Counter.count)
        
C1 = Counter()
C2 = Counter()

''' 4) Write a program to demonstrate built-in attributes of a class .Access and 
    print the class name,objectID,and instance of an object'''
class Demo:
    pass
d1 = Demo()
print("\n Class Name :",Demo.__name__)
print("Object ID :",id(d1))
print("Is d1 an instance of Demo?", isinstance(d1,Demo))

''' 5) Write a program for simple inheritance .Create a base class representing 
    a person with basic details and a derived class representing a student that adds academic related data'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,sid,studying_year):
        self.name=name
        self.age=age
        self.sid=sid
        self.studying_year=studying_year
    def display(self):
        print("\nStudent Details")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Student ID :",self.sid)
        print("Studying Year :",self.studying_year)
s1 = Student("Santosh", 20, "S01", 2)
s1.display()

''' 6) Write a program to demonstrate the multiple inheritance where one class representing a person 
    and another represents a teacher .The derived class should inherit both functionalities 
    and display teacher and person details'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Teacher:
    def __init__(self,subject,experience):
        self.subject=subject
        self.experience=experience
class PT(Person,Teacher):
    def __init__(self,name,age,subject,experience):
        self.name=name
        self.age=age
        self.subject=subject
        self.experience=experience
    def display(self):
        print("\nTeacher Details")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Subject :",self.subject)
        print("Experience :",self.experience)
t1 = PT("Jaya", 35, "Computer Science", 10)
t1.display()

''' 7) Write a program to generate random numbers within a given range .Allow
    the user to specify the range and number of random numbers to be generated'''
import random
def generate_random_numbers(start, end, count):
    random_numbers = []
    for _ in range(count):
        random_numbers.append(random.randint(start, end))
    return random_numbers
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
count = int(input("Enter the number of random numbers to generate: "))
random_numbers = generate_random_numbers(start_range, end_range, count)
print("Generated random numbers:", random_numbers)

''' 8) Write a program to use the math module to calculate the area and circumference of a circle
    Take the radius as input from the user'''
import math
def area(r):
    return math.pi * r**2
def circumference(r):
    return 2 * math.pi * r
radius = float(input("Enter the radius of the circle: "))
print("Area of the circle:", area(radius))
print("Circumference of the circle:",circumference(radius))

''' 9) Write a program to validate a phone number using regular expressions
    Ensure the number follows the format XXX-XXX-XXXX '''
import re
text = "Phone number are : 798-193-5534  and   another one 6034543-243 " 
pattern = r'\b\d{3}-\d{3}-\d{4}\b'
result = re.findall(pattern,text)
print(result)

''' 10) Write a program that accepts a list of students scores and perform the following tasks:
    '''
# a) Sort the list in ascending order
scores = [85, 92, 78, 90, 88,85,78]
sorted_scores = sorted(scores)
print("Sorted scores:", sorted_scores)
#b) Identify and remove duplicate scores
unique_scores = list(set(scores))
print("Unique scores:", unique_scores)
# c) Calculate the average score
average_score = sum(scores) / len(scores)
print("Average score:", average_score)

''' 11) Write a program to create a class representing a bank account .
    Implement methods to deposit ,withdraw , and check the balance of the account'''
class BankAccount :
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. Current balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdraw: {amount}. Current balance: {self.balance}")
B1 = BankAccount()
B1.deposit(50000)
B1.withdraw(20000)

''' 13) Write a program to simulate a simple library system .Implement classes for Book
    and Members Allow members to borrow and return Books and track which books are currently borrowed'''
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False
class Member:
    def __init__(self,name):
        self.name=name
        self.borrowed_books=[]
    def borrow_book(self,book):
        if book.is_borrowed:
            print(f"Sorry, {book.title} is already borrowed.")
        else:
            book.is_borrowed=True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
    def return_book(self,book):
        if book in self.borrowed_books:
            book.is_borrowed=False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

