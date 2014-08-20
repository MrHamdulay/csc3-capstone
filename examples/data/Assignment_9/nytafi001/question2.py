""" A program to reformat a text file so that all lines are at most a given length. Do not break up words.
Author: Afika Nyati
Date: 10th May 2014"""


def main():
    
    input_filename = input("Enter the input filename:\n")   # Assigns the name of the input filename given by the user to a variable.
    
    output_filename = input("Enter the output filename:\n") # Assigns the name of the output filename given by the user to a variable.
    
    width = eval(input("Enter the line width:\n"))  # Assigns the name of the line width given by the user to a variable.
    
    reformatter(input_filename, output_filename, width)     # Places all those variables as parameters into a function that reformats and prints out sentences into lines of a given length.
    

def reformatter(Input, Output, Width):      # A function that reformats and prints out sentences into lines of a given length.
    
    # Opens the file
    
    file = open(Input, "r")     # Opens the file with the sentences and assigns the file to the 'file' variable.
    input_file = file.read()    # Assigns the contents of the file to a variable.
    file.close()    # Closes the file.
    
    
    # Manipulating the contents of the file
     
    input_file = input_file.split("\n\n")  # Splits the string on the double newline characters, which represent new paragraphs. Therefore you end up with a list of paragraphs.
   
    for paragraph in range(len(input_file)):    # A definite loop that splits each string of words in each paragraph in the list to a list of words.
        
        input_file[paragraph] = input_file[paragraph].split("\n")   # For each paragraph, it splits the paragraph at the newline character, representing a new line in the paragraph.
        
        input_file[paragraph] = " ".join(input_file[paragraph])    # Joins the list of each line in each paragraph into one long string representing each sentence in the paragraph
        
        input_file[paragraph] = input_file[paragraph].split(" ")    # Splits the long string of words in the paragraph into a list of strings representing each word in the paragraph.
    
    
    # Reformatting the passage and putting it into the output file.    
    
    char = 0    # Initialzes a char variable to zero. This variable represents the current amount of characters in the current line.
    
    output_file = open(Output, "w")     # Open the output file.
    
    
    
    for paragraph in range (len(input_file)):     # A definite loop that goes through each paragraph.
        
        
        for word in input_file[paragraph]:  # A definite loop that goes through each word in the input_file and prints it out in lines of a given length.
        
            
            if char + len(word) == Width:   # If the characters in the line + the length of the next word (without space) will not exceed the chosen width:
                                 
                char += len(word)    # Add the length of the current word to the character variable.
                            
                print(word, end = "", file = output_file)      # Add the current word to the output file.            
                continue    # Stops the loop from entering any other decisions under this one.
            
            if char + len(word) +1 > Width:     # If the characters in the line + the length of the next word and a space will exceed the chosen width:
                
                char = len(word) + 1    # Reset the amount of characters and add the length of the current word.
                
                print("\n" + word, end =" ", file = output_file)    # Go to the next line and add the current word to the output file.
                continue    # Stops the loop from entering any other decisions under this one.
            
            else:   # If the characters in the line + the length of the next word and a space will not exceed the chosen width:
                                     
                char += len(word) + 1   # Add the length of the current word to the character variable.
                                
                print(word, end = " ", file = output_file)      # Add the current word to the output file.            
                
        
        print("\n", file = output_file)     # Adds a newline character at the end of the text file, to go to a new paragraph.
        char = 0    # Reinitialzes a char variable to zero.
    
    output_file.close()     # Close the output file


main()
    
    