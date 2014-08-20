"""question 1-assignment 7- unique list
GVNPRI022
02 May 2014"""

word=input(("Enter strings (end with DONE):\n\n"))
unique=[]
found=-1
while(word!="DONE"):   #end loop when 'DONE' entered
    
    for i in range (len(unique)):
        if (word==unique[i]):  #cehcking if word is unique
            found=0
            
    if (found ==-1): #adding new word
        
        unique.append(word)
    found=-1
    word=input()   

print("Unique list:")
for j in range(len(unique)):
    print(unique[j])
    