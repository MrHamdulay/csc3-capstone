#Joy Arendse-Gorvalla
print("Independent Electoral Commission")
print("-"*32)
n=input("Enter the names of parties (terminated by DONE):\n") #asking for input

DICT={} #creating a dictionairy
while n!="DONE": #loop for when the input doesnt equal "DONE"
    if n not in DICT:
        DICT[n]=1 
    else: DICT[n]=DICT[n] + 1
    n=input() 

L=[] #creating a list

for i in DICT: #definite loop
    L.append(i) #adds all "i" from dictionary to the list
L.sort() #puts list in alphabetical order

print() #prints a blank line
print("Vote counts:")

for j in L:
    print(j," "*(12-len(j)-len(str(DICT[j]))), "- ", DICT[j], sep="")
