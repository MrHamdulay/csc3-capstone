"""Assignment 9, Question 2
Jadon Thomson
14-05-2014"""

string = ''       #create a string to build up and then write to file.

def write_out(out_filename, s, w):
    """Takes input string and formats it too correct line length.
    Then writes this new string to the ouput file"""
    global string
    if len(s) < w:
        file2 = open(out_filename, "w")
        string = string + s
        file2.write(string)
        file2.close
    else:                      #This else makes sure that when there is a new line the measuring of lengths of strings starts again after the new line.
        if '\n\n' in s[:w]:
            for i in range(len(s[:w])):
                if s[i:i+2] != '\n\n':
                    string += s[i]
                else:
                    string += '\n\n'
                    return write_out (out_filename,s[i+2:],w)
        else:
            for i in range (w,0,-1):
                if s[i] == ' ':
                    string = string + s[:i] + '\n'
                    return write_out(out_filename,s[i+1:],w)
                else:
                    continue

        
def main():
    """Takes input, creates a string from the contents of the file. 
    Removes carrige returns but leaves double carrige returns so as to keep 
    paragraphs"""
    in_filename = input ("Enter the input filename:\n")
    out_filename = input ("Enter the output filename:\n")
    w = eval(input ("Enter the line width:\n"))  
    file = open (in_filename, "r")
    s1 = file.read()
    s1 = s1.replace('  ','~~')               #all the s1.replace statements are making sure that the final string keeps in paragraph seperaters (i.e. '\n\n') and that any double spaces are kepts. They also ensure that the new string has no carrige returns other than those notifying a new paragraph.
    s1 = s1.replace('\n\n','**')
    s1 = s1.replace('\n',' ')
    s1 = s1.replace('**','\n\n')
    s1 = s1.replace("  "," ")
    s1 = s1.replace('~~','  ')
    file.close()
    write_out(out_filename, s1, w)
    
main()