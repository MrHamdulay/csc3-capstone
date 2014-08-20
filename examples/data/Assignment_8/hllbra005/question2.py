# Program that uses a recursive function to count the number of pairs of consecutive characters in a string
# Brandon Hall (HLLBRA005)
# 09/05/2014

def Doubles(text, position, count): # This method is used to count the doubles in the text
    
    if (position + 2 > len(text) ): #Make sure the sentance does not end
      
        return count  
     
    else: 
        
        if ( (text[position]) == (text[position+1]) ): # This checks if double letters 
            
            count +=  1
            position += 2  # Incease the position by 2 - pairs cannot overlap, therefor it moves on to the next possible set
            
            return Doubles (text, position, count)

        else: # If there isn't a pair, i.e The char at position doesnt = char at (position + 1)
            
            position = position +1 # Increase the position by 1 so that the program will check this new position with the next character
            
            return Doubles(text, position, count)

    
def Main():
    
    text = input("Enter a message:\n") 

    count = Doubles(text, 0,0) 

    print("Number of pairs:", count) 

Main()