print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):\n")

x = ""
dictionary = {}
x = input()

while x != "DONE":
    
    
    if x in dictionary:
        dictionary[x]+=1
    elif x not in dictionary:
        dictionary[x]=1    
    x = input()


ordereddictionary = sorted(dictionary)


print("Vote counts:")
for j in ordereddictionary:
    length = len(j)
    print(j," "*(11-length),"- ",dictionary.get(j,""),sep="")
    
    
    #print(" {0:>11}".format(dictionary.get(j,"")))
    #print(len(j))