# string=input("Enter string:")
# char=0
# word=1
# for i in string:
#       char=char+1
#       if(i==' '):
#             word=word+1
# print("Number of words in the string:")
# print(word)
# print("Number of characters in the string:")
# print(char)


l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))
a=[(x,x**2) for x in range(l_range,u_range+1)]
print(a)