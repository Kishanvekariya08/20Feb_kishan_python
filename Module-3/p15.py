'''Write a Python program to get unique values from a list'''
list1=[]   
list2=[]
size=int(input("enter number of element: "))
for i in range(size):
    li=input("enter element values: ")
    list1.append(li)

for i in list1:
    if i not in list2:  
        list2.append(i)
print(list2)