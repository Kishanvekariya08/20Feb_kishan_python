'''Write a Python function that takes two lists and returns true if they have 
at least one common member.'''
lis1=[] 
lis2=[]
size=int(input("enter number of element: "))

for i in range(size):
    get1=input("enter list 1 element values: ")     
    get2=input("\nenter list 2 element values: ")
    lis1.append(get1)  
    lis2.append(get2)   
print(f"list 1: {lis1}")
print(f"list 2{lis2}")
if lis1[-1]==lis2[-1]: 
    print("true")
else:
    print("false")