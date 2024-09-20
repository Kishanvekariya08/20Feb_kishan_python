'''Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30.'''

lis=[] 
for i in range(1,31):
    square=i*i
    lis.append(square)
print(lis[:5])     
print(lis[-5:])    
