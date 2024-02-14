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

#Python Program to Replace Every Blank Space with Hyphen in a String

string=input("Enter string:")
string=string.replace(' ','-')
print("Modified string:")
print(string)

#How to Reverse a String in Python

a=str(input("Enter a string: "))
print("Reverse of the string is: ")
print(a[::-1])


#Python Program to Calculate the Length of a String Without using Library Functions
string=input("Enter string:")
count=0
for i in string:
      count=count+1
print("Length of the string is:")
print(count)


#ython Program to Determine How Many Times a Given Letter Occurs in a String Recursively
def check(string,ch):
      if not string:
        return 0
      elif string[0]==ch:
            return 1+check(string[1:],ch)
      else:
            return check(string[1:],ch)
string=input("Enter string:")
ch=input("Enter character to check:")
print("Count is:")
print(check(string,ch))

#Python Program to Calculate the Length of a String Without using Library Functions
string=input("Enter string:")
count=0
for i in string:
      count=count+1
print("Length of the string is:")
print(count)

#Python Program to Count the Number of Words and Characters in a String

string=input("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)

#Python Program to Count Number of Lowercase Characters in a String
string=input("Enter string:")
count=0
for i in string:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:")
print(count)

#Python Program to Count the Number of Vowels in a String


string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)

#Python Program to Count Number of Uppercase and Lowercase Letters in a String
string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)

#Python Program to Check if the Substring is Present in the Given String

string=input("Enter string:")
sub_str=input("Enter word:")
if(string.find(sub_str)==-1):
      print("Substring not found in string!")
else:
      print("Substring in string!")
      
#Python Program to Find Common Characters in Two Strings

s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)
    
#Python Program to Print All Letters Present in Both Strings
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)|set(s2))
print("The letters are:")
for i in a:
    print(i)
    
#Python Program that Displays which Letters are in First String but not in Second
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)-set(s2))
print("The letters are:")
for i in a:
    print(i)
    
    
#Python Program that Displays Letters that are not Common in Two Strings
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)^set(s2))
print("The letters are:")
for i in a:
    print(i)
    
    
#Python Program to Create a New String Made up of First and Last 2 Characters

string=input("Enter string:")
count=0
for i in string:
      count=count+1
new=string[0:2]+string[count-2:count]
print("Newly formed string is:")
print(new)


#Python Program to Sort Hyphen Separated Sequence of Words in Alphabetical Orde

def change(string):
      return string[-1:] + string[1:-1] + string[:1]
string=input("Enter string:")
print("Modified string:")
print(change(string))

#String Palindrome Program in Python
string=input("Enter string:")
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")

#python Program to Check if Two Strings are Anagram

s1=input("Enter first string:")
s2=input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")
      
#Python Program to Check whether a String is Palindrome or not using Recursion

def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")


def  sum_of_element(arr , n):
    sum = 0
    for i in n:
        sum = sum + arr[i]
    return sum
arr =[28+23+26+2662+22]
n=arr(l)
print (sum_of_element(arr,n))
