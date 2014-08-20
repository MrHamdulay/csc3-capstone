#Chantel Foot
#Question 2 
#Assignment 8 

def count_pairs(x):
    if len(x) == 1: #if the string has only 1 letter, there are no pairs. 
        return 0 
    
    elif len(x) ==2:
        if x[0] == x[1]: #if the string has 2 letters, and the 2 letters are equal then theres 1 pair 
            return 1
        
        else:
            return 0 #not equal and only 2 letters, not a pair 
        
    elif x[0] == x[1]: #first letter equals 2nd letter
        return 1 + count_pairs(x[2:]) # return 1 cause 1st pair and then call count pair function but starting at position 3 
    else:
        return count_pairs(x[1:]) #count pairs at the next one after current position 
    
x = input ("Enter a message:\n") #outside loop 
print("Number of pairs: ",end = "")
print(str(count_pairs(x)))



