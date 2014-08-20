#Formating File
# Sofia Palmer
#14 May 2014

infile = input("Enter the input filename: \n")
outfile = input("Enter the output filename: \n")
line_width = input("Enter the line width: \n")

infile = open(infile, "r")
lines = infile.readlines ()
outfile = open(outfile, "w")

count = 0
newstring = []
spaces = 0


for i in range(len(lines)):
    lines = lines.split(" ")
    for j in range(len(lines[i])):
        lines[i][j] = word
        count += len(word)
        if word == "\n":
            del word["\n"]
        if word == " ":
            count += 1
            while (count != line_width):
                newstring.append(word)
            
        
   
            
    







    
    



                
 
       
       
       
       

                        
                        
                        
                        
                
        
        
        








