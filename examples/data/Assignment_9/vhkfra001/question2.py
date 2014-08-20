'''
program to reformat a text file so that each line is at most a certain length
frans van hoek
13 may 2014
'''

def get_file():
    
    # get file name from user
    fname = input("Enter the input filename:\n")
    
    # then get contents
    file = open(fname, "r")
    
    # append text to a string without the \n's and a space between
    text = ''
    for line in file.readlines():
        line2= " " + line[:-1]
        text += line2
        
    file.close()
    
    # return the text as a single string
    return text


def align(text):
    
    # split the text into a list of seperate words
    words1 = text.split(" ")
    words = []
    
    # remove all empty strings from the list
    for n in range(len(words1)):
        if words1[n] != '':
            words.append(words1[n])
    
    # ask user for output file
    global output 
    output = input("Enter the output filename:\n")
    
    # ask user for line width
    width = eval(input("Enter the line width:\n"))
    
    # define new empty string and line length counter
    ans = ""
    linelen = 0
    
    # go through list and add \n whenever the max line length is reached
    for word in words:
        x = linelen + len(word)
        if x < width:
            new = word + " "
            ans += new
            linelen += len(new)
        else:
            new = "\n" + word + " "
            ans += new
            linelen = len(word) + 1
            
    return ans


def write(text):
    
    # overwrite the output file with new text
    f = open(output, "w")
    print (text, file=f)
    f.close()


def main():
    x = get_file()
    y = align(x)
    write(y)
    
    
if __name__ == "__main__": main()