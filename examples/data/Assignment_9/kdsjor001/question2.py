"""Assignment 9 Question 2
10 May 2014
Jordan Kadish, Reformatting Textwrap"""

InFile=input('Enter the input filename:\n')
OutFile=input('Enter the output filename:\n')
LineWidth=eval(input('Enter the line width:\n'))
Line=0
f=open(InFile,'r')
lines = f.readlines()
f.close()
for i in range (len (lines)-1):
    lines[i] = lines[i][:-1] #Getting rid on \n character
Words=[]
for i in range(len(lines)):
    if lines[i]=='':
        Words.append(['\n\n']) #for paragraph checking
    else:
        Words.append(lines[i].split(' '))
f=open(OutFile, 'w')
for i in range(len(Words)):
    for j in range(len(Words[i])):
        if Line==0:
            Line=len(Words[i][j])+1
            print(Words[i][j],end=' ',file=f) #The first word of a paragraph
        elif Words[i][j]=='\n\n':
            Line=0
            print(Words[i][j],sep='',end='',file=f) #Printing the paragraph blank line
        elif len(Words[i][j])+Line>LineWidth: #Wrapping step
            print('\n',Words[i][j],sep='',end=' ',file=f)
            Line=len(Words[i][j])+1
        else:
            if len(Words[i][j])+Line<=LineWidth: #Wasn't sure about the trailing spaces problem
                Line+=len(Words[i][j])+1         #so just to be safe
                print(Words[i][j],end=' ',file=f)
            else:
                print(Words[i][j],end='',file=f)
f.close()

