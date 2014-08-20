""" A program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates.
Author: Afika Nyati
Date: 1 May 2014"""

def main(): 
    
    List = enter_strings() # Assigns the list created by the enter_strings function to a variable.
    print_list(List) # Prints the List variable in the correct order
    

def enter_strings():  # Creates a list of strings, without duplicates
    
    List = []  # Initializing a list variable
    
    Entry = input("Enter strings (end with DONE):\n") # Asks user for the first entry
    
    while Entry != "DONE": # A sentinel loop that continues to ask the user for an entry and checks whether that entry is already in the list until it encounters the sentinel.
        
        if Entry in List: # Checks whether the entry is already in the list
            Entry = input("") # Asks user for another entry, without the prompt
            
        
        else: # If the entry isn't in the list
            
            List.append(Entry) # The entry is added to the list.
            Entry = input("") # Asks user for another entry, without the prompt
        
    
    print() # Prints a blank line
        
    return List
        


def print_list(List): # Prints the List variable in the correct order
    
    print("Unique list:") # Initial heading
    
    for value in List: # Loops through the values in the list
        
        print(value) # Prints the value
        


main()
        