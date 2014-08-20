'''Formatting files
Irfan Habib
2014/05/16
'''
name = input("Enter the input filename:\n")
output = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
#data capture
r = open(name, 'r')
wf = open(output, 'w')
wrds = r.read()
wrds = wrds.split('\n')#split into list
wrds1 = []
for wrd in wrds:
    if wrd != '':
        wrds1 = wrds1 + (str(wrd).split(' '))
    else:
        wrds1.append('\n\n')

ln = 0
for w in wrds1:#loop through list and print words
    if w == '':
        wf.write(' ')
        ln+=1
        continue
    elif w == '\n\n':
        wf.write(w)
        ln = 0
        continue
    ln += len(w)
    if ln==(width-1):#if line is 40 chars long, print and go to new line
        wf.write(" "+w+"\n")
        ln = 0
    elif ln==len(w):
        wf.write(w)#for first word printed, space second
    elif ln<width:#if line is shorter, print word
        wf.write(" "+w)
        ln +=1#increase length value because of space 
    else:
        wf.write("\n"+w)#when word cannot fit on line, go to new line
        ln = len(w)#length value is of word length with space
        
r.close()
wf.close()#closing to preserve resources and finish writing