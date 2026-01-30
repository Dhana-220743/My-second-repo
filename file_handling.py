file=open("file1.txt","w")
print("File is created")
file.write("Hey girlllllll!!!!!!!")
f1=open("f1.txt","w")
f1.write("Hey hiiiiii!!!!")
f1=open("f1.txt","r")
'''
print(f1.read())
f1=open("f1.txt","a")
f1.write("\n I love you")
f1=open("f1.txt","r")
 print(f1.readline())
for i in f1:
    print(i)

try:
    f1=open("f1.txt","x")
    print("File is created")

except FileExistsError:
    print("File is already exists")

lines=0
words=0
characters=0
for i in f1:
    lines+=1
    words=words+len(i.split())
    characters=characters+len(i)
print("Lines:",lines)
print("Words:",words)
print("Characters:",characters)'''
search=input("Enter the word to be searched:")
found=False
for i in f1:
    if search in i:
        print("Word is found")
        found=False
        break
    if found:
        print("Word  found")
    else:
        print("Search completed wrd not found")
file.close()
f1.close()