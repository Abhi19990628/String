# modify string is :odd no in string value 

def modify(string):
    final=""
    for i in range (len(string)):
        if i % 2 ==0:
            final=final+string[i]
    return final 
string=input("enter the string :")
print("yuor modify string is :")
print(modify(string))


#Python Program to Remove the nth Index Character from a Non-Empty String

def remove(string , n):
    first= string[:n]
    last=string[n+1:]
    return first+last
string=input("enter the values:")
n=int(input("enter the text no you want remove:"))
print("modify string is :")
print(remove(string , n))

#replace 
string=input("Enter string:")
string=string.replace('a','$')
string=string.replace('A','$')
print("Modified string:")
print(string)

string=input("enter striung :")
string=string.replace('a', '$')
string=string.replace("a",'$')
print(string)