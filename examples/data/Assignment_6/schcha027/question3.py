#Charles Schleich SCHCHA027
#Question 3 Assignment 6

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
sentence=""
party_array=[]
party_list=[]
# while loop that fills party_array with user inputs
# and fills party list, with one instance of each unique entry for party array
while sentence!= "DONE":
    sentence=input("")
    if  sentence !="DONE":
        party_array.append(sentence)    
        if sentence not in party_list:
            party_list.append(sentence)
            
print()
party_list.sort()
print("Vote counts:")
# For loop runs through every item in party array an compares to pary list
# counts the number of each in party array
for i in range(len(party_list)):
    item =party_list[i]
    count=0
    for j in range( len(party_array)):
        if item==party_array[j]:
            count=count+1
#        
    print(item," "*(10-len(item))," - ",count,sep="")    
        
