#Kovlin Perumal
#21/04/14
#Question1 - Alignment program

names = []
name = input("Enter strings (end with DONE):\n")

maxlen = 0

while( name!='DONE') : #Populate names array
   
   names.append(name) 
   
   if(int(maxlen) < int(len(name))) : #Find max length
      maxlen = len(name)
      
   name = input()#Ask for input again with no text

print("\nRight-aligned list:") 

for i in range(len(names)) :
   if(len(names[i]) < maxlen) :
      names[i] = " " * (maxlen - len(names[i])) + names[i] #Create spaces according to max name length 
      
   print(names[i])

