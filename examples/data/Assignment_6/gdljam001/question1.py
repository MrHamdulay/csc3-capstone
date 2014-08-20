"""Alignment of inputed strings
James Godlonton
23 April 2014"""

def enterStrings(): #Function to input strings the print them right aligned
    print("Enter strings (end with DONE):\n")#Header
    inp="" #Value of each input
    inpCol=[] #Collection of all inputs
    while inp!="DONE": #Loop until stop sentinal is entered, each time add the string to the collectoin
        inp=input("")
        if(inp!="DONE"):
            inpCol.append(inp)
    
    longest=0
    for word in inpCol: #Loop through collection checking for the largest length
        if(len(word)>longest):longest=len(word)
        
    print("Right-aligned list:")    
    for inp in inpCol:# Go through entire collection printing them formatted right with highest length as width 
        outp=("{0:>"+str(longest)+"}").format(inp)
        print(outp)
        
        
if __name__=="__main__":
    enterStrings()