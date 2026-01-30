'''n=int(input("Enter number of elements:"))
l1=[]
for i in range(n):
    ele=int(input("Enter element:"))
    l1.append(ele)
print("List elements are:",l1)
lst=[1,4,3,3,5]
print("Original list:",lst)
print(list(set(lst)))
student={}
n=int(input("Enter number of students:"))
for i in range(n):
    key=input("Enter student name:")
    value=int(input("Enter student marks:"))
    student[key]=value
print("Student details are:",student)'''

lst=["apple","banana","apple","apple"]
d={}
for i in lst:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)