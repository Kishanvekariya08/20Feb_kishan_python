#Write a python program to find the longest w.

f = open("txt.text",'r')  

max_l = 0  
l_word = ""  

for line in f:
    w = line.strip().split()    
    for word in w:
        if len(word) > max_l:
            max_l = len(word) 
            l_word = word 
        elif len(word) == max_l:   
            l_word += " " + word

print("Longest word : ",l_word)  