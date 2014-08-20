#CHARLES SCHLEICH
#SCHCHA027

import re
infilename= input("Enter the input filename:\n")
outfilename=input("Enter the output filename:\n")
linewidth=eval(input("Enter the line width:\n"))
#asks user for input of input file, output file and line width

file=open(infilename,"r")


def align(textBlock):
       
        printText=""
        #string slicing including spaces and characters as unique entries
        # i.e. string=['hello',' ','world','!']
        string=re.split(r"(\s+)", textBlock)
        sent=""        
        for i in range(len(string)):
                
                if string[i]=="\n": # just a new line
                    sent=sent+" "        
                    #printText=printText+"\n"
                    
                elif string[i]==' \n':# space then new line
                    
                    sent=sent+" "
                    
                elif string[i]=="":#just empty string
                    sent=sent+""
                    printText=printText+sent+"\n"
                   
                    
                elif (len(sent)+len(string[i]))>linewidth and string[i]==" " :
                    printText=printText+sent+"\n"
                    sent=""        
                   
                elif (len(sent)+len(string[i]))>linewidth:# case where temp string(sent+string at i) is max length
                 
                    printText=printText+sent+"\n"
                    sent=""+string[i]
                    if i == (len(string)-1):
                            printText= printText+sent
                    
                elif (len(sent)+len(string[i]))<=linewidth: #  case where temp string(sent + string at i) is still inside length
                    sent=sent+string[i]
                    
                    if i == (len(string)-1):
                            printText= printText+sent
                    
                    
        return printText
    

text=file.readline()
final_text=""
textBlock=""
#This While Loop Breaks the Text up into paragraphs, processes the paragraphs then produces the final printable aligned text
while text!="":
    if text[0]=="\n":
        final_text=final_text+"\n"+align(textBlock)
        textBlock=""
    else:
        textBlock=textBlock+text
    text=file.readline()
    
final_text=final_text+"\n"+align(textBlock)
file.close()
outfile=open(outfilename,"w")

#code Starts by adding a newline character 

print(final_text[1:],file=outfile)
outfile.close() 