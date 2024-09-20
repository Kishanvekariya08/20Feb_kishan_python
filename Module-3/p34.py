#Write a Python script to check if a given key already exists in a dictionary.

dic={'id':1,'name':'kishan','age':21}

key=input("enter you finde key:")  

if key in dic:     
    print("\nkey are exists in dictionary")
else:
    print("\nkey are not exists in dictionary")