
letter=input("Enter a message: \n")   
    
def count_pairs(letter):
    if len(letter)<2:   #if there is less than two words or an empty string dont do anything this is the base case using boolian
        return  0
    

    elif letter[0] == letter[1]:    #when satisfies the pairs condition any where in the string
        
        return 1 + count_pairs(letter[2:])  #iteratively the number will increase by 1 but each time the string will get smaller as a recursive step, the recursive step starts after the pair has been found in order for the program to be more efficient, imagine if we started after the 1st word another condition has to be met to avoid confusion

    else:
        return 0 + count_pairs(letter[1:]) #this is still a recursive step when no pairs where found 
            
            
    
print("Number of pairs:",count_pairs(letter))   #display
    
    
    
    
    
    
    
