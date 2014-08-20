"""Assignment 6 Question 3
Count Votes per Candidate
Shaheen Karodia
KRDSHA003
2014_04-20"""

print("Independent Electoral Commission")
print("--------------------------------")
x=input("Enter the names of parties (terminated by DONE):\n")
candidates=[]
output_test=[]
if x!="DONE":
    candidates=[x]



while x!="DONE":
    
    x=input("")
    
    if x=="DONE":
        candidates.sort()  #sort list into aplhabetical order
        break
    else:
        candidates.append(x)
                            
                            
print()
print("Vote counts:")

for i in candidates:
    if i in output_test: #check to see if candidate has already been seen once in the list
        continue

    else: 
        output_test.append(i)
        print(i, (10-len(i))*(" "), " - ", candidates.count(i), sep="") #prints votes justified in a collumn of width 10
    
    