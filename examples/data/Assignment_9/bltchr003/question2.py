"""Reformating a text file
Chris Bolton
BLTCHR003"""



import textwrap



infile_name=input("Enter the input filename:\n")

outfile_name=input("Enter the output filename:\n")

w=eval(input("Enter the line width:\n"))



infile= open(infile_name, "r")

lines=infile.readlines()  
infile.close()



outfile= open(outfile_name, "w")

words=""                       
for i in range(len(lines)):

    if lines[i]=="\n":         

        paragraph=textwrap.wrap(words, width=w)

        for j in range(len(paragraph)):

            if j==len(paragraph)-1: 

                print(paragraph[j], "\n", file=outfile) 

            else:

                print(paragraph[j], file=outfile)

           

        words=""                

        

    else:

        words+=lines[i]  
        

final=textwrap.wrap(words, width=w)  

for k in final:

    print(k, file=outfile)

        

    

outfile.close()