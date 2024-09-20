'''How will you remove last object from a list? 
Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?'''

list1 = [] 
no=int(input("enter number of element:"))
for i in range(no):
    li=input("enter element values:")
    list1.append(li)    

print(f"list : {list1}")
print(f"listy last element: {list1[-1]}")

list1.pop()
print(f"list after removing last element: {list1}")

