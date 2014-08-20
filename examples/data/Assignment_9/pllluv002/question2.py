"""Textfile line limiter
By: Luveshen Pillay
10/5/14"""

# Opening of files and output layout
infileinput=input("Enter the input filename:\n")
infile=open(infileinput,"r")
outfileinput=input("Enter the output filename:\n")
outfile=open(outfileinput,"w")
z=infile.read()
w=eval(input("Enter the line width:\n"))


#Body of program to limit line
def linelimeter(z):
    try:    
        if z== "":
            print("")
        
        if z[w] == " ":

            r=z.replace("\n"," ")  
            print(r[:w+1],file=outfile)
            return linelimeter(z[w+1:])
            
        if z[40]!= " ":
                
            r=z.replace("\n"," ")            
            search=r[w-6:w]
            spacefinder=search.find(" ")
            cut=w-5+spacefinder
            print(r[:cut],file=outfile)
            return linelimeter(z[cut:])
        
    except:
        r=z.replace("\n"," ") 
        print(r[:],file=outfile)
        
    
    
        
        
        
linelimeter(z)
        



outfile.close()

    
    