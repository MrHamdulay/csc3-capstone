#Question 3
#Tauriq Dolley
#CSC1015F
#Assignment 6

print("Independent Electoral Commission")
print("--------------------------------")

names = {}
vote = 1
sentinel = 'DONE'
names[input("Enter the names of parties (terminated by DONE):\n")] = 1

while sentinel not in names:                #terminates when user enters DONE
    newname = input("")

    if newname not in names:                    #if the party name is already present in dictionary
        names[newname] = 1 
    elif newname == "DONE":     
        break    
    else: 
        namevalue = names[newname]        
        names[newname] = namevalue + 1

del names["DONE"]


print()
print("Vote counts:")
x = "{0: <10} - {1:>}"
for i in sorted(names):
    print(x.format(i,names[i]))

    
    