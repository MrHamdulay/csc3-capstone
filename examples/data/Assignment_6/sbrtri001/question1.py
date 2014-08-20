''' Assignment 6, question 1
Reads in a list of names and prints them right-aligned
Tristan Subroyen
19 April 2014 '''

def stringList(): # This function inputs a list of names, and then prints them right-aligned
    
    # initializations:
    array = []
    maxLength = 0
    arrayCount = 0
    string = ""
    # Ask user for input, terminated by DONE
    print("Enter strings (end with DONE):")
    while string != 'DONE':
            string = input() # user input
            array.append(string)
            arrayCount += 1 # Keeps count of how many items in the array
            
            # Determine the name which is longest for alignment:
            if len(string) > maxLength:
                maxLength = len(string)
                
    array.remove('DONE') # Remove DONE from array
    arrayCount = arrayCount-1 # Minus one for indexing
    # For output:
    print('')
    print("Right-aligned list:")
    
    # Print the list of names, aligning them as well:
    for i in range (arrayCount):
        difference = maxLength - len(array[i]) # difference in length between name and longest name...
        print(" "*difference + array[i])                            
               
if __name__ == "__main__":
    stringList()
            
        
        
        
    