"""program to reformat a text file-paragraphing
nasha somoina meoli
11th may 2014"""

def reformat_paragraph():
    f = open(input("Enter the input filename:\n"),"r")
    f2 = open(input("Enter the output filename:\n"),"w")
    #to get a grid
    lines = f.readlines()
    
    paragraph =""
   
    #join lines into paragraph without consisdering lengths
    for line in lines:
        if line != "\n":
            line = line.replace("\n"," ")
            paragraph+= line
        else:
            paragraph+=line
   
    f.close()
    counter = 0
    new_paragraph = ""
    paragraph = paragraph.split(" ")
    
    width = eval(input("Enter the line width:\n"))
    #format paragraph to required width
    for a in range(len(paragraph)):
        counter +=len(paragraph[a])
        s = paragraph[a]
    # formatting if it is a new paragraph    
        if s.count("\n") ==1:
            counter = 0
            paragraph[a].replace("\n","")
            new_paragraph+="\n"+paragraph[a]+" "
            counter+=len(paragraph[a])
    #formatting of the paragraph body
        elif counter<=width:
            new_paragraph+=paragraph[a]+" "
            counter+=1
        else:
            counter = 0
            new_paragraph+="\n"+paragraph[a]+" "
            counter+=len(paragraph[a])+1
    print(new_paragraph,file=f2)
    f2.close()
    
reformat_paragraph()
                
            
    