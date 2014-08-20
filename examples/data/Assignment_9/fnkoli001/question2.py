"""
Oliver Funk
FNKOLI001
Assignment 9 - Files
"""

#Get user input
read_file = input("Enter the input filename:\n")
write_file = input("Enter the output filename:\n")
line_width = int(input("Enter the line width:\n")) + 1 # Have to add 1, i don't know why...


#read file
file = open(read_file)
file_data = file.read()
file.close()


#Proccess text

# Splits paragraphs into list
temp_paragraphs = file_data.split("\n\n")  

# Replaces all the return characters with spaces
paragraphs = []
for para in temp_paragraphs:
    paragraphs.append(para.replace("\n", " "))
    
# Splits a list of words of each paragraph up when line_width has been reached
formatted_paragraphs = []
for para in paragraphs:    
    formatted_para = []    
    words_list = para.split(" ")
    
    while words_list: # While there are still words in words_list
        # Cumlitive count of the length of the words
        length_counter = 0
        
        #Numbers of words before the split
        no_words = 0
        
        #Add the correct line to formmatted_para
        line = []
        for word in words_list:
            length_counter += len(word) + 1
            if line_width >= length_counter:
                line.append(word)
                no_words+=1
            else:
                break
            
        #Appends the line to formatted_para, separated with spaces
        formatted_para.append(" ".join(line))
        
        #Sets the the list equal to the the same list but starting with the word right after where the return character must go
        words_list = words_list[no_words:]
    
    formatted_paragraphs.append("\n".join(formatted_para))


#Write to file
file_to_write = open(write_file, "w")
print("\n\n".join(formatted_paragraphs), file=file_to_write)
file_to_write.close()