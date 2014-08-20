#Assignment 9, Question 2
#James Nevin
#12 May 2014

input_file = input("Enter the input filename:\n")
f = open (input_file, "r") #Opening the file
lines = f.readlines()
f.close() #Reading lines into list before closing
output_file = input("Enter the output filename:\n")
f = open (output_file, "w") #Creating new file
width = int(input("Enter the line width:\n")) #Finding width

counter = 0 #Characters printed per line
for line in lines:
    if line != '\n': #If not a new line
        pre_letter = "##"
        for i in range (len(line)-1):
            if line[i] == line[i+1] and line[i] == " ":
                pre_letter = line[i-1]
        line = line.split() #Split each line into words
        for word in line:
            if counter + len(word) < width: #If space for word and a space
                counter += len(word) + 1
                print (word, file = f, end = " ") #Print word with space, increase counter
            elif counter + len(word) == width: #If no space for space
                counter = 0
                print (word, file = f, end = "\n") #Print word with no space
            elif len(word) == width: #If just space for word, print on single line
                print ("\n" + word, file = f)
                counter = 0
            else:
                counter = len(word) + 1
                print ("\n" + word, file = f, end = " ") #Else, go to next line and print
            if (word[-1] == pre_letter):
                print (" ", file = f, end = "")
    else: 
        print ('\n', file = f) #Print paragraphs
        counter = 0
f.close() #Close file