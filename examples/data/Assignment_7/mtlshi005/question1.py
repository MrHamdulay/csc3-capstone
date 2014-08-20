#Shivaan Motilal
#Programme to remove duplicates
#27/04/14
#Create list
listo=[]

print("Enter strings (end with DONE):")

#user inputs words
while True:
    word=input()
    
    if word=="DONE": break 
        
    else:
        if word not in listo:
            listo.append(word)

#Counts number of diff words in list and adds to a dictionary
print()



#Print out new list
print("Unique list:")
for word in listo:
    print(word)

        
        
    