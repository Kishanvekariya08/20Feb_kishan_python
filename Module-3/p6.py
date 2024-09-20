'''Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings.'''

str1=input("enter first string: ") 
str2=input("enter secand string: ")    

print(f"first string lenth :{len(str1)}")  
print(f"secand string lenth :{len(str2)}")  

if str1[0]==str2[0] and str1[-1]==str2[-1]:
    print("string first and last character are same")
else:
    print("string first and last character are not same")
