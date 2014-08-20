"""  a program that uses a recursive function to count the number of pairs of 
repeated characters in a string
Author: Dominic Manthoko
05 May 2014"""

def pair(mes):
    """ a function that checks for pairs of repeated characters"""
    
    if mes == '' or len(mes) < 2:      
        return 0
    
    elif mes[0] == mes[1]:                 
        return pair(mes[2:]) +1        # if the first two character of a string are the same
                                       # return 1 and call the pair function on the rest of the string excluding the first two characters
    
    else:
        return pair(mes[1:])
    
if __name__ == "__main__":
    # prompt the user to enter a message
    mes = input("Enter a message: \n")    
  
    print("Number of pairs:",pair(mes) )
        
