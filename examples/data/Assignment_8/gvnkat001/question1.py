""" A program with a recursive function to calculate whether or not a string is a palindrome 
Katlego Gaveni 4th May 2014"""



def palindrome(string):  # A recursive function that checks whether in inputted string is a palindrome. 
    
    if len(string) <= 1: # stoping condition when there is one letter in the string .
        
        return True
    
    else:
       
        return string[:1] == string[len(string)-1:len(string)-2:-1] and palindrome(string[1:len(string)-1]) 
    
    

def main():
    
    string = input("Enter a string:\n") #user input
    
    if palindrome(string) == False: # If the palinrome recursive function returns False, print "Not a palindrome!"
        
        print("Not a palindrome!")
        
    else: # If the palinrome recursive function returns True, print "Palindrome!"
        print("Palindrome!")
    
main()