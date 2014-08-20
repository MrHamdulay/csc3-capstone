"""a program to reformat a text file so that all lines are at most a given length
Zikho Godana
15 May 2014"""

input_filename=input("Enter the input filename:\n")
input_file=open(input_filename,"r")
content=input_file.readlines()
input_file.close()

#get rid of the "\n" character printed at the end of each item in content
for i in range (len(content)):
    content[i] = content[i][:-1]
    
string=" ".join(content)
l=string.split()

output_filename=input("Enter the output filename:\n")
width=input("Enter the line width:\n")

for j in range(0,len(string),int(width)):
    #line=string[0+j:int(width)+j]
    if j==0:
        line=string[0+j:int(width)-1]
    else:
        if " " in string[int(width)+(j-3):int(width)+j] and string[int(width)+(j-1)]!=" ":
            line=string[0+j:int(width)+(j-1)]
             
        else:
            line=string[0+j:int(width)+j]
    #print(line)

    output=open(output_filename,"a")
    print(line,file=output_filename)
    output.close()