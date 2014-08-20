#Description: Reformat a text file into another file with lines of a given length.
#Name: Paul Roux - RXXPAU008
#Date: 15 May 2014

def reformat_txtfile(input_file,output_file,width):
    """Reformats the contents on a given text file to a specific line width and writes it to another file"""
    contents = []
    string = ''
    formatted = []
    
    try: #Used in case the user enters a filename that doesn't exist
        f = open(input_file)
        for i in f.readlines():
            contents.append(i)
        f.close()            
    except:
        print("File not found") 
    
    for j in contents:#Used to keep the places of paragraphs
        if j == '\n':
            j = '/NewLine '
        j = j.strip('\n')
        if j[len(j)-1]!=' ':
            string = string+j+' '
        else: string = string+j
    
    string = string.replace('  ',' #-#')#Used to keep places for double spaces
    words = string.split()
    out = ''
    
    for i in range(len(words)):#Formats the text as is required
        if words[i] == '/NewLine':
            out = out+'\n'
            formatted.append(out)
            out = ''
        else:
            out = out+words[i].replace('#-#',' ')
            try:
                if len(out+' '+words[i+1]) > width:#Checks if adding another string will make the the line longer that the desired width
                    formatted.append(out)
                    out=''
                else: out = out+' '
            except: formatted.append(out)   
    
    w = open(output_file,'w')
    for i in formatted:#Writes the formatted lines of text to the new file
        w.write(i+'\n') 

if __name__ == '__main__':
    in_file = str(input("Enter the input filename:\n"))
    out_file = input("Enter the output filename:\n")
    width = int(input("Enter the line width:\n"))
    
    reformat_txtfile(in_file,out_file,width)