'''Daniel Feinstein FNSDAN001
Assignment 9
Text Align
'''

#Open files and get input
infile = open(input("Enter the input filename:\n"), "r")
outfile = open(input("Enter the output filename:\n"), "w")
width = int(input("Enter the line width:\n"))

#INITIALISATION
total = 0
cnt = 0

lines = infile.readlines()


for line in lines:
    
    x = line.split(" ")
    
#check each word and add length to total to see if we can print the word.
    for word in x:
        if word == "\n":
            print(word, file = outfile)
            total = 0
            cnt = 0
        else:
            if len(word.replace("\n", ""))+total <= width:
                if cnt == len(x)-1:
                    print(word.replace("\n", ""),end = "")
                    total += len(word.replace("\n", ""), file = outfile) +1
                
                else:
                    
                    print(word.replace("\n", ""), end = " ", file = outfile)
                    total += len(word.replace("\n", "")) +1


            
            else:
                print("\n", end = "", file = outfile)
            
                if cnt == len(x)-1:
                    print(word.replace("\n", ""),end = "" ,file = outfile)
                    total = len(word.replace("\n", "")) +1
                
                else:
                  
                    print(word.replace("\n", ""), end = " ", file = outfile)
                    total = len(word.replace("\n", "")) +1
            cnt+=1

            cnt = 0
#close files
infile.close()
outfile.close()
    
        

