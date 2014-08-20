'''program to reformat a text file into lines of a given length
tom new
2014/05/11'''

def gettext (filename):
    '''returns the contents of a text file as a string'''
    
    # imports the file as a string of characters
    file = open (filename, 'r')
    lines = file.read ( )
    file.close ( )
    i = 0
    while i < len (lines):
        
        # preserves paragraphs
        if lines [i:i + 2] == '\n\n':
            lines = lines [:i] + lines [i + 1:]
            
        # else strips newlines
        elif lines [i] == '\n':
            lines = lines [:i] + ' ' + lines [i + 1:]
        i += 1        
    return lines

def reformat (s, w):
    '''sends a string of words to a list where each element is at most w characters long'''
    
    wrapped = []
    i = 0
    while True:
        
        # checks if it is the last line
        if s [i + 1:] == '':
            wrapped.append (s)
            return wrapped # kills the loop and returns wrapped
        
        #checks if paragraph
        elif s [i] == '\n':
            wrapped.append (s [:i + 1])
            wrapped.append ('\n')
            s = s [i + 1:]
            i = 0
            
        # iterates i if line not long enough
        elif i + 1 != w:
            i += 1
            
        # checks if the next character is a space
        elif s [i + 1] == ' ':
            wrapped.append (s [:i + 1] + '\n')
            s = s [i + 2:]
            i = 0
            
        # checks if the wth character is a space
        elif s [i] == ' ':
            wrapped.append (s [:i] + '\n')
            s = s [i + 1:]
            i = 0
            
        # checks if previous character is a space
        elif s [i - 1] == ' ':
            wrapped.append (s [:i - 1] + '\n')
            s = s [i:]
            i = 0
            
        # else character must be 'inside' a word
        else:
            
            # iterates back through the word to find the previous space
            while s [i] != ' ':
                i -= 1
            wrapped.append (s [:i] + '\n')
            s = s [i + 1:]
            i = 0

if __name__ == '__main__':
    infilename = input ('Enter the input filename:\n')
    outfilename = input ('Enter the output filename:\n')
    width = eval (input ('Enter the line width:\n'))
    outfilelines = reformat (gettext (infilename), width)
    outfile = open (outfilename, 'w')
    for line in outfilelines: # writes the wrapped lines to outfile
        print (line, file = outfile, end = '')
    outfile.close ( )