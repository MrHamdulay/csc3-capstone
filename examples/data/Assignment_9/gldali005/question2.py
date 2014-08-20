#Ali Goldstein
# program to reformat a text file so that all lines are at most a given length. Do not break up words. Write the formatted text to a new text file.
#15 May 2014

#opens the file 
inputfile=input("Enter the input filename: \n")
outputfile=input("Enter the output filename: \n")
wid=eval(input("Enter the line width: \n"))
f=open(inputfile, "r")
#stores the entire file as a single string
text=f.read()
f.close()

#opening file to wrtie in it
ff=open(outputfile, "w")
#prints the line of the file up to the line width entered by the user
if text[wid]!=" ":
    for i in range(wid-1):
        print(text[i], end="",file=ff)
else:
    for i in range(wid):
        print(text[i],end="",file=ff)
ff.close()   


            
        

        
    
        
        




