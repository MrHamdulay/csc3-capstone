"""Michael Odhiambo
ODHMIC003
Assignment 9_Question 2"""
filename= input("Enter the input filename:\n")#Prompt user for input
output= input("Enter the output filename:\n")
line_width= eval(input("Enter the line width:\n"))
fob= open(filename,"r")
read= fob.readlines()
strings=[]
"""Remove "\n" from strings and append strings to array"""
for i in read:
    string= i.rstrip("\n")
    if len(string)>0:
        if string[-1]!=" ":
            strings.append(string+" ")
    elif len(string)==0:
            strings.append("\n"+"\n")
print(strings)        
n_strings= "".join(strings)#Convert array to string
line= []
place= line_width*1
"""Recursive function used to format strings into the required length and append them to an array"""
def insert(n_strings,line_width):
    if len(n_strings)>line_width:
        line_width=place
        if n_strings[line_width]!=" ":
            while n_strings[line_width]!=" ":
                line_width= line_width-1
        line.append(str(n_strings[0:line_width])+("\n"))
        insert(n_strings[line_width:],line_width)
    elif len(n_strings)==line_width:
        line_width=place
        line.append(str(n_strings[0:line_width]))
    elif len(n_strings)<line_width:
        line_width=place
        line.append(str(n_strings[:])) 
insert(n_strings,line_width)
message=[]
"""Remove gaps at the beginning of new lines and append lines to an array"""
for i in line:
    if i[0]==" ":
        i= i[1:]
        message.append(i)
    else:
        message.append(i)
"""Join lines in array into paragraphs"""
ans= "".join(message)
fob.close()
fob2= open(output,"w")
fob2.writelines(ans)
fob2.close()

    
    
#C:\input.txt
#C:\output.txt
#C:\Users\Michael O\Desktop\output.txt