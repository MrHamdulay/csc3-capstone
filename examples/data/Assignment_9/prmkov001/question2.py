#Kovlin Perumal
#PRMKOV001
#13/05/2014
#File Alignment Program


original = input("Enter the input filename:\n") #Open the original textfile for reading purposes 

f = open (original,"r")
text=f.read() #Read the contents into a single variable
f.close ()

outputFile = input("Enter the output filename:\n") 
width = eval(input("Enter the line width:\n")) #Ask for required input

text = text.replace("  "," * ")
text = text.replace("\n"," ") #Replace double spaces and new line charecters to allow for splitting into a words array using spaces as the seperaters

f = open(outputFile,"w") #Open the output textfile in write mode

words = text.split(" ") #Split into an array using spaces

length = 0

for i in range(0,len(words)): 
    
    if words[i] == "*" :
        words[i] = "  " #Replace the * with the original double space

    if words[i]=="  ":
        print(" ",end="",file=f)#If theres a double space we need two spaces not one
        
    elif words[i]=='':
        print("\n",file=f) #If theres an empty string value in words go to the next line
        length=0 #initialise length back to zero
        
    elif(words[i]!=" "):
        
        if length+len(words[i])<=width: #Make sure existing length and length of word added less then width entered
            
            print(words[i]," ",sep="",end="",file=f)
            
            length+=len(words[i])+1 #Increase current length
        else:
            print("\n",words[i]," ",sep="",end="",file=f) #If it exceeds width print the word on the next line and reinitialise length to the length of the word
            length = len(words[i])+1
        
f.close()