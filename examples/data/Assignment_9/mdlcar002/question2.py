'''
16 May 2014
Assignment 9 Question2
Program to reformat a text file
MDLCAR002
'''
inputN = input("Enter the input filename:\n")
outputN = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

r = open(inputN, 'r') #the input file is only for reading purposes
wf = open(outputN, 'w')#the output file is to write to
words = r.read()
words = words.split('\n')#converts the string into a list
words1 = []
for word in words:
    if word != '':
        words1 = words1 + (str(word).split(' '))
    else:
        words1.append('\n\n')

length = 0
for w in words1:   #this loops through list and prints the words
    if w == '':
        wf.write(' ')
        length+=1
        continue
    elif w == '\n\n':
        wf.write(w)
        length = 0
        continue
    length = length + len(w)
    if length==(width-1):#if line is longer than the width its prints and goes to a new line 
        wf.write(" "+w+"\n")
        length = 0
    elif length==len(w):
        wf.write(w) #for first word printed, space second
    elif length<width: #if line is shorter, print word
        wf.write(" "+w)
        length +=1 #increase length value due to the space 
    else:
        wf.write("\n"+w)#this is for when the word cannot fit on the line,goes to new line
        length = len(w)#length value is of word length with space
        
r.close()
wf.close()