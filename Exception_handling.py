'''
    a=int(input("Enter number"))
    b=int(input("Enter number"))
    c=a/b
except:
    print("Error occurred")
    
try:
    a=input( "Enter String:")
    b=int(input("Enter number:"))
    c=a+b
except:
    print("Cant add string and number")
    
a=[1,2,3]
try:
    print("First element:",a[1])
    print("fifth element:",a[4])
except:
    print("Array index out of bound")
    '''

