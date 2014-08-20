"""program to reformat a text file so that all lines are at most a given length
Gary Finkelstein
13 May 2014"""

#Enter file names:
inputFile = input("Enter the input filename:\n")
outputFile= input("Enter the output filename:\n")
#Enter width
lineWidth=eval(input("Enter the line width:\n"))

#open file and put values in array
f=open(inputFile,"r")
inputString = f.readlines()
inputString[-1]+=("\n")
f.close()
newArray=[]
for i in range (len(inputString)):
    
    inputString[i]=inputString[i][:-1]
    newArray.append(inputString[i].split(" "))

totalString=""
#write to file
f=open(outputFile,"w")
for i in range (len(newArray)):
    if(len(newArray[i])==1 and newArray[i][0]==""):
        print("",file=f)
    for j in range(len(newArray[i])):
        if((len(totalString)+(len(newArray[i][j])))==lineWidth):
            
            totalString+=newArray[i][j]
            
        
        elif (len(totalString)+(len(newArray[i][j]))+1)<lineWidth:
            
            totalString+=newArray[i][j]+" "
            
        else:
            #totalString=totalString[:-1]
            print (totalString,file=f)
            totalString=newArray[i][j]+" "
           
         
          #put new string into textfile
        
        if(i==(len(newArray)-1))and (j==(len(newArray[i])-1)):  
            
            print(totalString,file=f)
          
          
f.close()



