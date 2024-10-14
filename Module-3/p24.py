#Write a Python program to convert a list to a tuple.

no=int(input("neter number of element in list:"))
lis=[] 

for i in range(no):
    data=input("enter list element values:")
    lis.append(data)
print("tupel:",tuple(lis))  
print("list:",lis)