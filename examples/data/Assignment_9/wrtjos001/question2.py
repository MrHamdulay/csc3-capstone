"""Assignment 9 Question 2 a program to reformat a text file so that all lines are at most a given length
joshua wort
11 May 2014"""

#input statements
input_f=input("Enter the input filename:\n")
output_f=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

#open and read input file
input_file=open(input_f,"r")
lines=input_file.read()
input_file.close()

#overwrite output file
output_file=open(output_f,"w")

#create paragraphs when there are two newline tabs
paragraph=lines.split("\n\n")

i=0
while i<len(paragraph):
    lines=paragraph[i].split(" ") #split each word
    lines=" ".join(lines)
    lines=lines.replace("\n"," ") #replace newline tabs with a space
    lines=lines.split(" ") #create a list
    j,k=0,0
    while j<len(lines):
        while k<=width:
            #break out of loop when all words have been written to output file  
            if j>=len(lines):
                break  
            #add 1 to j when the word is a space, thereby effectively decreasing length of lines by 1 
            if lines[j]==" ":
                j+=1
                
            #print line to output file until length equals line length
            if len(lines[j])<=width-k:
                print(lines[j], file=output_file, end=" ")
                k+=(len(lines[j])+1)
                j+=1
            else:
                print("\n",lines[j], file=output_file ,sep="",end=" ") #create a new line when maximum words per line is reached  
                k=(len(lines[j])+1)                
                j+=1 
            #reset variable k to zero    
            if k>=width:
                k=0
                print(file=output_file)             
    print("\n",file=output_file) #print newline when line paragraph is completed
    i+=1
output_file.close()

            
                
                   

        
                                
        
        
    
    
                
    

    


    
        


        
    




