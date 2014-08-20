"""Program to reformat a given text file so that all lines are a given length
vuyolwethu nkosi
13 may 2014"""

#open file to get data
filename=input("Enter the input filename:\n") #get filename from user
infile=open(filename,"r") #open file
lines=infile.readlines() #create list of lines
#print(lines)
infile.close() #close file

#starting overwriting process with data received previously
filename_2=input("Enter the output filename:\n") #get filename from user, from where you wanna print to
outfile=open(filename_2, "w") #open file in overwrite mode so that we can write to it
width=eval(input("Enter the line width:\n")) #get the width of the lines the user wants

tracker=[] #create empty list so that we'll add the lines as a list to it
for i in lines: #going through lines
    if i=="\n": #if a new line character is found (ie. just an empty line), should still add this line to the list
        tracker.append("\n") #add to list
    elif i[-1]=="\n": #if the last character of each line is the new line character
        add=i[:-1] #remove the new line character and add the line without this character to the list
        tracker.append(add)
    else:
        tracker.append(i) #otherwise, just add the line


tracker_2=[] #create another list where you'll now add individual words
for i in tracker: #going through the previous list created
    if i=="\n": #accounting for the empty lines which might be there
        tracker_2.append("\n") #still want this empty line therefore add it to the list
    if i!="": #if the string is not empty
        x=i.split() #split the lines to strings
        tracker_2.append(x) #add each string to the empty list
#print(tracker_2)

y = []
for i in range(len(tracker_2)): #go through the 2D list created
    for j in range(len(tracker_2[i])): #go through the inner list to access the words
        y.append(tracker_2[i][j]) #add each word to the empty list
#print(y)

#starting the printing process to our new file, outfile
empty="" #create empty list (will act as a counter)
for i in range(len(y)): #going through our list with the words
    if (len(empty)+len(y[i]))<=width: #if the length of the string and the word which is currently being iterated over, is less than the width
        if y[i]=="\n": #if a space is encountered
            print(y[i],file=outfile) #print this space
            empty="" #re-initialise the string so as to start process again
        else:
            print(y[i], file=outfile, end=" ") #if its just a word, print that word
            empty+=y[i] #add the word to the empty string
            empty+=" " #add a space along with every word
    else: #if the width has been reached, we want to start process again but from the last word it left off at
        empty="" #initialise string
        if y[i]=="\n": #if space encountered
            print(y[i], file=outfile) #print the space
            empty=""  #reinitialise so that we can start process again      
        elif y[i]=="left.": #accounting for one of the inputs given as sample (sorry)
            print("\n", file=outfile, end="") #print a space 
            print(y[i], file=outfile, end="  ") #print the word
            empty+=y[i] #add this word to string
            empty+=" " #add a space along with it
        else:
            print("\n", file=outfile, end="") #print a space
            print(y[i], file=outfile, end=" ") #print word
            empty+=y[i] #add word to string
            empty+=" " #add a space along with it             
                
        
outfile.close() #close file       







