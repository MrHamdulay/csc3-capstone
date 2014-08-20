'''
Created on 12 May 2014
Text file re-formatting
@author: Yusuf Khan
KHNYUS005
'''
name = input("Enter the input filename:\n")
output = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
#all input and integer evaluations above
r = open(name, 'r')
wf = open(output, 'w')#opening of files and declaring modes
wrds = r.read()
wrds = wrds.split('\n')#add all words in input to list
wrds1 = []
for wrd in wrds:
    if wrd != '':
        wrds1 = wrds1 + (str(wrd).split(' '))
    else:
        wrds1.append('\n\n')

length = 0
for w in wrds1:#loop through list and print words
    if w == '':
        wf.write(' ')
        length+=1
        continue
    elif w == '\n\n':
        wf.write(w)
        length = 0
        continue
    length = length + len(w)
    if length==(width-1):#if line is 40 chars long, print and go to new line
        wf.write(" "+w+"\n")
        length = 0
    elif length==len(w):
        wf.write(w)#for first word printed, space second
    elif length<width:#if line is shorter, print word
        wf.write(" "+w)
        length +=1#increase length value because of space 
    else:
        wf.write("\n"+w)#when word cannot fit on line, go to new line
        length = len(w)#length value is of word length with space
        
r.close()
wf.close()#closing to preserve resources and finish writing