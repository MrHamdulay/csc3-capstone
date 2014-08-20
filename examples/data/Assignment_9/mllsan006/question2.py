#a program to reformat a text file so that all lines are at most a given length
#sankara mallane
#12 may 2014

inputFile = input('Enter the input filename:\n') # user input for input file name

outputFile = input('Enter output filename:\n') # user input for output file name

lineWidth = eval(input('Enter the line width:\n')) #the line length provided by the user 

#open the input file for reading
file = open(inputFile,'r')
#Read entire file into a list of strings
lines = file.readlines()
file.close()

#empty array
words = []

for theLine in lines: # the for loop appends a zero 
    if theLine == '\n': # when the newline is a paragraph
        words.append(0)

    for theWord in theLine.rstrip().split(' '):# if not a paragraph we add the words
        words.append(theWord) # from that line

# opening the output file in order to write to the file
file = open(outputFile,'w')

count = 0 # a counter
theLine = ''
for i in range(len(words)):# looping in the range of length words
    theWord = words[i]
    
    if type(theWord) == int: # there is a newline character when the word is an integer
        
        print(theLine.rstrip(),file=file,sep='') # print the line to the file
        print(file=file,sep='')
        count = 0 # reset counter
        theLine = '' # reset the line
      
    # the elif statement checks that the word can fit on the line given the line width       
    elif count + len(theWord) + (1 if 0<count else 0) < lineWidth + 1: # when the counter is greater than zero a space must be added however when it is zero a space does not need to be added as the first word of the line is added
        
        if count>0: # the if statement checks if the counter is greater than 0
            
            theLine += ' ' # to add a space before the word
            count += 1
            
        count += len(theWord) # the word is being added to the line
        theLine += theWord
        
    else: # the else statement prints the line to the file
        # resets the line and resets the counter
        print(theLine.rstrip(),file=file,sep='')
        theLine = theWord 
        count = len(theWord)
        
print(theLine.rstrip(),file=file,sep='') #  the remaining line is then printed

# file must be closed when done
file.close()












