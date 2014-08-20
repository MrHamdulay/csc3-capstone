# program to reformat a text file so that all lines are at most a given length
# mllgad001
# 14 May 2014

#get file names
infileName = input("Enter the input filename:\n")
outfileName = input("Enter the output filename:\n")
width = input("Enter the line width:\n")

# open the files
infile = open(infileName, "r")
outfile = open(outfileName, "w")

# read the entire file into one string and replace new line characters with empty string
line = infile.read()


new_line1 = line.replace('\n', ' ')
new_line = new_line1.replace('  ', ' \n\n ')


split_line = new_line.split(" ")    # split string into separate strings in a list


width_field =0 
list_ = []
for item in split_line:            # iterates through each item in list
    if item == '\n\n':
            print(" ".join(list_), file = outfile)   # prints the previous line                    
            list_ = [item]
            width_field = len(item) 
            
    elif width_field + len(item) + 1 <= int(width):   # as long as the width field is less than the line width
            list_.append(item)     # add the item to the list
            width_field += len(item) + 1                # adds 1 to account for the empty space 
            
     # if max width length is reached, add the first word of next line into the list as empty string and carry on with loop
    else:
        print(" ".join(list_), file = outfile)   # prints the previous line                    
        list_ = [item]
        width_field = len(item)    
        
for item in list_:      # prints out the last line that was stored in the list
    print(item, end =" ", file = outfile)
    
# close the files
infile.close()
outfile.close()