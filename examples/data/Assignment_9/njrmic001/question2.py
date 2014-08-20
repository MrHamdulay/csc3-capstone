#A program to reformat a text file so that all lines are at most a given length
#Author: Michelle Njoroge
#14 April 2014

f=input("Enter the input filename:\n")
g=input("Enter the output filename:\n")

input_file=open(f,"r")
list1=[]
for line in input_file:
    for i in range(len(line)):
        if line[i]=="\n":
            line2=line[:i]
        elif line[i]!="\n":
            line2=line
    list1.append(line2)
string=(" ").join(list1)

input_file.close()    

input_file=open(f,"r")

paragraph=[]
width=eval(input("Enter the line width:\n"))

def reformat(string):
    global width
    if len(string)<=width:
        paragraph.append(string)
    elif len(string)>width:
        if string[width]!=" ":
            while string[width]!=" ":
                width=width-1
            paragraph.append(string[:width])
            return reformat(string[width+1:])
        elif string[width]==" ":    
            paragraph.append(string[:width])
            return reformat(string[width+1:])
    return paragraph
input_file.close()

input_file=open(f,"r")
output_file=open(g,"w")

reformat(string)
for line in paragraph:
    print(line,file=output_file)

input_file.close()
output_file.close()



           