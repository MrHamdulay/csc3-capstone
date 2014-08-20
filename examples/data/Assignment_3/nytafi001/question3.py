# A program to draw frame (made of the characters +-|) around a message that has been repeated on consecutive lines.
# Author: Afika Nyati
# Date: 21 March 2014

def main():
    
    message = " " + input("Enter the message:\n") + " "
    repeat = eval(input("Enter the message repeat count:\n"))
    thick = eval(input("Enter the frame thickness:\n"))
    
    lenfirstbox = len(message)
    
    dashcount1 = lenfirstbox + 2*(thick - 1)
        
    
    #Top
    for i in range(thick): # For the top of the frame. This code makes all the lines before words.
            
        print("|"*i+"+"+"-"*dashcount1+"+"+"|"*i)
                        
        dashcount1-=2
        
    # Middle    
    while (repeat>0): # An indefinite loop repeating message as many times as stipulated.
        
        print("|"*thick + message + "|"*thick)
        
        repeat-=1
        
    dashcount2 = lenfirstbox
    
    # Bottom
    for i in range(thick,0,-1): # For the bottom of the frame. This code is the opposite of the top of the frame.
                    
        print("|"*(i-1)+"+"+"-"*dashcount2+"+"+"|"*(i-1))
                               
        dashcount2+=2            


main()