"""reformat a text file
kennedy muranda
17/5/2014"""

#input from the user
inputFile = input('Enter the input filename:\n') 
outputFile = input('Enter output filename:\n')
lineWidth = eval(input('Enter the line width:\n')) 


#open the input file for reading
file = open(inputFile,'r')
lines = file.readlines()
file.close()

#empty array
words = []

#loop appends 0
for theLine in lines: 
    if theLine == '\n': 
        words.append(0)

    for theWord in theLine.rstrip().split(' '):
        words.append(theWord) 


#open output file
file = open(outputFile,'w')


c = 0
theLine = ''
for i in range(len(words)):
    theWord = words[i]
    
    if type(theWord) == int:
        
        print(theLine.rstrip(),file=file,sep='') 
        print(file=file,sep='')
        c = 0 
        theLine = '' 
      
         
    elif c + len(theWord) + (1 if 0<c else 0) < lineWidth + 1: 
        if c>0: 
            
            theLine += ' ' # to add a space before the word
            c += 1
            
        c += len(theWord) # the word is being added to the line
        theLine += theWord
        
    else: # the else statement prints the line to the file
    
        print(theLine.rstrip(),file=file,sep='')
        theLine = theWord 
        c = len(theWord)
        
        
print(theLine.rstrip(),file=file,sep='') 


#close file
file.close()












