#Shaylan Lalloo
#15/05/2014
#Gets each line to have less than a inputted number of characters

filename = input('Enter the input filename:\n')
#get filename

f = open(filename, 'r')
#open file

myin = f.read()
#read file to string

f.close()

hasfound = False
mystrings = ''
for i in myin:
    if hasfound == True:
        hasfound = False
        if i != ' ':
            mystrings += ' '
        if i == '\n':
            mystrings += '\n'
    if i != '\n':
       mystrings += i
    else:
        hasfound = True
#gets rid of newline characters unless there are consecutive newlines

myout = ''
#current line

i = 0
#character in word

mycur = ''
#current word

filename = input('Enter the output filename:\n')
#get output filename

f = open(filename, 'w')
#open file for writing

width = int(input('Enter the line width:\n'))
#get line width

while i < len(mystrings):
    if i < len(mystrings):
        while mystrings[i] == ' ':
            mycur += ' '
            i += 1
            if i == len(mystrings):
                break
        #increase word to start with spaces
    if i < len(mystrings):
        while mystrings[i] != ' ':
            mycur += mystrings[i]
            i += 1
            if mycur[-1] == '\n':
                break
            if i == len(mystrings):
                break
        #find when word ends by looking for next space
    if mycur[-1] == '\n':
        if len(myout) + len(mycur) - 1 <= width:
            myout += mycur
            print(myout, file = f)
            myout = ''
            mycur = ''
        else:
            print(myout)
            print(mycur)
        #if hit a newline character, output accordingly
    if len(myout) >= 1:
        while myout[0] == ' ':
            myout = myout[1:]
        #get rid of spaces at end of lines
    if len(myout) + len(mycur) <= width:
        myout += mycur
        mycur = ''
        #check if word can go in current line. If does just put it
    else:
        print(myout, file = f)
        myout = ''
        while mycur[0] == ' ':
            mycur = mycur[1:]
        myout += mycur
        mycur = ''
        #otherwise begin new word and output last line
    

if myout != '':
    print(myout, file = f)
#output if line is not empty

f.close()
#close file
