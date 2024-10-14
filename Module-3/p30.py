# Write a Python program to convert a list of tuples into a dictionary.

school = [(1,'kishan',True), (2,'viraj',False), (3,'rahul',False)]     

dict = {}
ran = 0
for i in range(1,len(school)+1):
    dict[i] = school[ran] 
    ran += 1  
print(dict)