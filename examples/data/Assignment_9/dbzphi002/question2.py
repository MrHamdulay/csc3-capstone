#Thembekile Dubazana
#dbzphi002
#Assignment 9:Q2

"""Reformat text file so lines are at given length"""

#The inputs

infile=input("Enter the input filename:\n")
outfile=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

#Get the lines
file=open(infile,"r")
edit=file.readlines()
file.close()



#Separate list by spaces
edit="".join(edit)
edit=edit.split() 

#Create the outfile with formated text
out=open(outfile,"w")
s=""
for i in range(len(edit)):
           if (len(s) + len(edit[i])) <= width:
                      s+= edit[i]+" "
           else:
                      print(s, file = out)
                      s = edit[i]+" "
                
#print the left over words   
print(s, file = out)
out.close()

file2=open(outfile,"r")
lines=file2.readlines()
for j in range(len(lines)):
           print(lines[j],end="")
        
            
    
