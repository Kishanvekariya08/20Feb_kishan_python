'''Write a Python function to get the largest number, smallest num and sum 
of all from a list.'''
l=[]   
size=int(input("enter number of element: "))    
for i in range(size):
    li=int(input("enter element values: "))   
    l.append(li)   

def states(num):
    ma=max(num)    
    sm=min(num)    
    su=sum(num)    
    return ma,sm,su
max,small,sum=states(l)
print(f"max number: {max}")       
print(f"sumall number :{small}")   
print(f"sum of number : {sum}"  )  