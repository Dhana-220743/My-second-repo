import re
''' 1) In the regex created from  ,What does group 0 cover ?
        group 1 ? Group 2?'''
pattern= r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
text = "Helllloooo 938-107-2590"
match=re.search(pattern,text)
print(match.group(0))
print(match.group(1))
print(match.group(2)) 

# 2) Find website URLs that begin with http:// or https://
text = "Login into github using github url https://github.com or else http://github.com"
pattern = r'https?:\/\/[^\s]+'
result = re.findall(pattern,text)
print(result)

'''3. Clean up dates in different date formats (such as 3/14/2015, 03-14-2015, and 2015/3/14) by
replacing them with dates in a single, standard format.'''
text = "The dates are 3/14/2015, 03-14-2015, and 2015/3/14"
pattern = r'(\d{1,4})[/-](\d{1,2})[/-](\d{1,4})'
result = re.sub(pattern,r'\1-\2-\3',text)
print(result)


#4)How would you write a regex that matches a number with commas for every three digits? It must match the following
# i) '42'
text = "number are  3,456 and another one is 1,234,123"
pattern = r'\b\d{1,3}(?:,\d{3})*\b'
result = re.findall(pattern,text)
print(result)

''' 5) How would you write a regex that matches the fullname of someone whose last name is
        "Nakamoto" and whose first name starts with a capital letter followed by lowercase letters? It must match the following:
    i) 'Santosh Nakamoto' 
    ii)'Alice Nakamoto'
    iii) 'robo Nakamoto' (should not match)'''
text = "The name is Santosh Nakamoto Alice Nakamoto and robo Nakamoto"
pattern = r'\b[A-Z][a-z]+ Nakamoto\b'
result = re.findall(pattern,text)
print(result)

'''6) How would you write a regex that matches a sentence where the first word is either 'Alice'
        ,Bob,or Carol the second word is either eats,pets, or throws ;the third word is apples,cats
        or baseballs and the sentence ends with a period ? This regex should be case sensitive it must
        match the following :
        'Alice eats apples
        Bob pets cats
        Alice throws Apples
        BOB EATS CATS(like this)        '''

text = "Alice eats apples. Bob pets cats. Alice throws Apples. BOB EATS CATS."
pattern = r'\b(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.'
result = re.findall(pattern,text)
print(result)
'''7. Strong Password Detection Write a function that uses regular expressions to make sure the
password string it is passed is strong. A strong password is defined as one that is at least eight
characters long, contains both uppercase and lowercase characters, and has at least one digit.
You may need to test the string against multiple regex patterns to validate its strength.'''
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
text = "StrongPass1"
if re.match(pattern,text):
    print("The password is strong.")



