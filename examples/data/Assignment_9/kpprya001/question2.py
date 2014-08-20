"""Ryan Kopping 13 May
program to write to a file using user-specified line lengths"""
#get the input from the user
inputFile = input("Enter the input filename:\n")
outputFile= input("Enter the output filename:\n")
lineWidth=eval(input("Enter the line width:\n"))
#read from the file
f=open(inputFile,"r")
inputString = f.readlines()
#append a new line character to the last character of the file(see line 16)
inputString[-1]+=("\n")
f.close()
newArray=[]
#delete all \n characters from the string and split it up into the array
for i in range (len(inputString)):
    
    inputString[i]=inputString[i][:-1]
    newArray.append(inputString[i].split(" "))

totalString=""
#write to the file
f=open(outputFile,"w")
for i in range (len(newArray)):
    
    if(len(newArray[i])==1 and newArray[i][0]==""):
        print("",file=f)
    for j in range(len(newArray[i])):
        #if the line is less then or equal to the length then add another word
        if (len(totalString)+(len(newArray[i][j]))+1)<=lineWidth:
            totalString+=newArray[i][j]+" "
           
         #otherwise if its greater then the length print the line to the file    
        else:
            totalString=totalString[:-1]
            print (totalString,file=f)
            totalString=newArray[i][j]+" "
         
          
         #if its the last line of the file print it
        if(i==(len(newArray)-1))and (j==(len(newArray[i])-1)):  
            
            print(totalString,file=f)
           
            
            
       
#close the file            
f.close()



