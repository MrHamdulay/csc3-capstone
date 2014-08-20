"""Tumi Mkhawana
14 May 2014
Assignment 9 question 2"""

#ask user for filename
infile= input("Enter the input filename:\n")
outfile= input("Enter the output filename:\n")
#ask user for width
width= eval(input("Enter the line width:\n"))

#read file
f= open(infile,"r")
lines= f.readlines()
f.close()

#write into output file
x= open(outfile,"w")
output=''
count=0


for i in lines:
    #remove newline character at the end
    i = i.replace('\n','')
    words = i.split(' ')
    for k in words:
        #check if length of string is still less than width
        if count+len(k) < width:
            output+=k+' '
            count+= len(k)+1
         #if length of string is equal to width, go to new line   
        elif count+len(k)==width:
            output+=k+'\n'
            count=0
        #if length of string is greater than row, append word to new row
        elif count+len(k) > width:
            output+='\n'+k+' '
            count=len(k)+1
print(output,file=x)
x.close()

        
