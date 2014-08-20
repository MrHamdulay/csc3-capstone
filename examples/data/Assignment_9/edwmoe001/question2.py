"""Program to format text file line width
Tauhirah Eguardo
2014/05/11
make array out of each word and length. Loop to get required line spacing - add length until width, then add words as single string to new list. 
work with list to get into text file."""

def wordlist(file):
    """takes file and puts each line in array then creates an array of all the words"""
    linearray = []
    linearray = list(file)# creates array of each line
    wordarray = []
    for i in range(len(linearray)):
        if len(linearray[i]) >1:
            linearray[i] = linearray[i][:-1]
        
        words = linearray[i].split(" ") # split splits according to spaces but retains "" if double space
        for j in range(len(words)):
            wordarray.append(words[j])
    return wordarray
                       
        
def linelist(array,width,file):
    """ needs to count for width according to len
    must take \n\n into account and restart after them"""
    if array != []:
        paragraph = False #boolean for paragraph check
        count = len(array[0]) + 1 #+1 here and line 47 for spaces
        line = ""   
        while count <= width: 
            if len(array) == 0: #checks for empty list
                break
            else:
                if array[0] != "\n":
                    if array[0] == "" : #checks for space from line 14 
                        line += " "
                    else:   
                        line += str(array[0]) + " "
                    
                    del array[0]
                    if array == []: #if reached last value
                        pass
                    else:
                        count += len(array[0]) + 1 #the next value
                    
                else:
                    file.write(line + "\n")
                    file.write("\n")
                    count = 0
                    del array[0]
                    paragraph = True
                    break
        if paragraph != True : #if true then nothing should be done because of line 14 & 15
            file.write(line + "\n")
        else:
            pass
        return linelist(array,width,file)
    else:
        file.close()
                   


def main():
    file_in = open(input("Enter the input filename:\n"),"r")
    file_out = open(input("Enter the output filename:\n"),"w")
    width = eval(input("Enter the line width:\n"))
    words = wordlist(file_in)
    arrayfile = []
    wordnumber = 0
    linelist(words,width,file_out)
    
    
main()
