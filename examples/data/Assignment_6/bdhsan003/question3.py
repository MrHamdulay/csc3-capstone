# program counting number of votes
# Sandisha Budhal
# BDHSAN003


print("Independent Electoral Commission")
print("--------------------------------")

#create empty list to enter the names of the different parties
the_list=[]
diff_parties=input("Enter the names of parties (terminated by DONE):\n") #ask user to input the names of the different parties

while diff_parties!="DONE":
        
        the_list.append(diff_parties)
        diff_parties=input("")

        
print()       
print("Vote counts:")

contr = {}

for word in the_list:
    if not word in contr:
        contr[word] = 1
    else:
        contr[word] += 1
        

for word in sorted(contr):
    print (word+" "*(10-len(word)),"-",contr[word]) 
    
    
    
    
        



