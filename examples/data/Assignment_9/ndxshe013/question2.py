def newline(string,position):
    if string[position] == " ":
        return string[:position] + "\n" + string[position:].strip()
    else:
        return newline(string,position-1)
def main():
    infilename = input("Enter the input filename: \n")
    outfilename = input("Enter the output filename: \n")
    width = eval(input("Enter the line width: \n"))
    file = open(infilename,"r")
    paragraph = file.read()
    file.close()
    
    
  
    paragraph = paragraph.strip()
    paragraph = paragraph.rstrip()
    paragraphs = paragraph.split("\n\n")
    
    file2 = open(outfilename,"w")
    file2.close()
    for paragraph1 in paragraphs:
        paragraph1 = paragraph1.replace("\n"," ")
        
      
        
        
        if width < len(paragraph1): paragraph1 = newline(paragraph1,width)
        
        while (paragraph1.rfind("\n") + width) < len(paragraph1):
            i = paragraph1.rfind("\n") + width + 1
            paragraph1 = newline(paragraph1,i)
        paragraph1 = paragraph1 + "\n"
        
        lines = paragraph1.split("\n")
        file2 = open(outfilename,"a")
        for i in lines:
            print(i,file = file2)
       
        file2.close()
    
            
main()

