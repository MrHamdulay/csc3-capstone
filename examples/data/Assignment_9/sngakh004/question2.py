"""Program to format length of lines in a supplied text file and write the formatted text to a new file.
Akhil Singh
SNGAKH004
15 May 2014"""

def formattext():
    
    
    in_file = open(input("Enter the input filename:\n"), "r") #Get location of the input file
    
    str1ng = in_file.readlines() # Read input file data into a list
    in_file.close()
     
    
    out_file = open(input("Enter the output filename:\n"), "w")# Get name of output file
    
 
    for s in range(len(str1ng)):                             #cleans up the list by deleting the leading spaces and the newline characters at the end of every line of the text.
        if str1ng[s][0] == " ":
            str1ng[s] = str1ng[s][1:]
        if str1ng[s][-1:] == "\n" and str1ng[s] != "\n":
            str1ng[s] = str1ng[s][:-1]
    

    str1ng = " ".join(str1ng)
    wrd_list = str1ng.split(" ")
    

    line_width = eval(input("Enter the line width:\n"))  #Get formatted line width.
    
    
    count = 0     # the count variable prints lines when a word is added and it causes the line width to exceed the specified line width. 
    lne = ""
    
    for w in range(len(wrd_list)):
        
        if wrd_list[w] == "\n":
            print(lne,"\n", file = out_file)
            
            lne = ""                        #Reset the current line and counter.
            count = 0
        
        
        elif count + len(wrd_list[w]) <= line_width:
            count += len(wrd_list[w])
            lne += wrd_list[w]
            if count < line_width:
                count += 1
                lne += " "
        
       
        else: # If adding the word causes the line o exceed the specified width, then print the old line and use the word to start a new line.
            print(lne, file = out_file)
            count = len(wrd_list[w])+1
            lne = wrd_list[w]+" "
    
   
    if lne:                                      #Print any remaining text 
        print(lne, file = out_file)
        
    out_file.close()
    
if __name__=="__main__":
    formattext()