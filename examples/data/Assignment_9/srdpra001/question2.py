'''
Prashanth Sridharan
SRDPRA001
Assignment 09
Question 02
'''

file_input = input("Enter the input filename:\n") #variable file_input asks the user for the input file name
f = open (file_input,"r") #variable f opens the input file and reads it at this point
intervals=f.read() #Variable intervals stores the file read into a single string.
f.close ()
file_output = input("Enter the output filename:\n") #variable file_output aks the user for the file name to be output
b = eval(input("Enter the line width:\n")) #variable b asks the width to be input.
intervals = intervals.replace("  "," $ ")
intervals = intervals.replace("\n"," ")
f = open(file_output,"w")
block = intervals.split(" ")  #variable block splits the contents of the file (ie the words) by a space character 
chrcters = 0 #variable chrcters initialised for counting the characters in the string.
if "$" in block:
    ind = block.index("$")
    block[ind] = "  "
for i in range(0,len(block)): #this loop prints to the output file.
    if block[i]=="  ":
        print(" ",end="",file=f)
    elif block[i]=='':
        print("\n",file=f)
        chrcters=0
    elif(block[i]!=" "):
        if chrcters+len(block[i])<=b:
            print(block[i]," ",sep="",end="",file=f)
            chrcters+=len(block[i])+1
        else:
            print("\n",block[i]," ",sep="",end="",file=f)
            chrcters = len(block[i])+1
f.close()