"""Question 2 - check for pairs of letters
Jembe Moran
11 May 2014"""

def checkpair(x):
    global count
    if len(x)>2: #if there are more than two letters to check
        if x[0]==x[1] or x[1]==x[2]: #check if 2nd letter is equal to 1st or 3rd
            count+=1 #if so, a pair
        checkpair(x[2:]) #check rest of string
    elif len(x)==2: #if only two letters left 
        if x[0]==x[1]: #check two letters for equality
                count+=1 #if so, a pair
    else: pass #finished
               
count=0
x=input("Enter a message:\n")
checkpair(x)
print("Number of pairs:", count)