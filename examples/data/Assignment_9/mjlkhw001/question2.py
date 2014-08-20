# Program to reformat text and make new file
# Khwezi Majola
# MJLKHW001
# 10 May 2014

def reform():
    filein = input('Enter the input filename:\n') #Gets the file name
    ffile = open(filein, 'r') #Opens the file to be read
    lines = ffile.readlines() #Reads the lines into a list of strings
    ffile.close #Closes the file
    out = [] #Empty list for later use
    
    fileout = input('Enter the output filename:\n') #Gets the output file
    l_width = int(input('Enter the line width:\n')) #Gets the line width
    
    string = ''
    print(lines)
    for i in range(len(lines)-1): #Makes list into string excluding the last entry
        a = lines[i]
        if a == '\n':
            string += ' ' + a + a #Ensures that spacing between paragraphs is maintained
        else:
            string += ' ' + a[:len(a) - 1] #Add each list entry to the string excluded the new line character
    string += ' ' + lines[len(lines)-1] #Add the last entry to the string
    
    string = string.replace('\n ', '\n') #Removes leading spaces at start of paragraps excluding the first
    
    string = string.lstrip() #Remove the leading space
    
    #Nature of this code requires string to be treated differently if there were seperate paragraphs in the input
    if '\n' not in string:
        while len(string) > (l_width):
            temp = l_width
            while string[temp] != ' ': #Find the position of the right-most space per line within the line width constraint
                temp -= 1
            out.append(string[:temp]) #Append up to and not including the found space
            string = string[temp+1:] #Remove characters before & including the space
    else:
        while len(string) > (l_width):
            if '\n\n' in string: 
                posn = string.find('\n\n') #Finds the position of the double new line character
            else:
                posn = l_width + 5 #If not in then posn is set to be greater than the length of one line
            temp = l_width 
            shift = False #Set boolean value to false
            if posn == 0: #If '\n\n' is at the start temp is increased by 4 so these characters don't affect the spacing 
                temp += 2
                shift = True #Set to true only if the string begins with '\n\n'
            while string[temp] != ' ': #Find the position of the right-most space per line within the line width constraint
                temp -= 1
            if temp > posn and shift == False: #The condition is only met if the postion is greater that new line characters and the postion of the new line characters isn't 0
                temp = posn - 1
            out.append(string[:temp]) #Append up to and not including the found space
            string = string[temp+1:] #Remove characters before & including the space
    out.append(string)  #Add the remainder
    
    for i in range(len(out)):
        if '\n\n' in out[i]: #Replace '\n\n' with '\n' as the print will act as and additional '\n'
            out[i] = out[i].replace('\n\n', '\n')
    
    ffile = open(fileout, 'w') #Open the file
    for a in out:
        print(a, file = ffile) #Print each line in
    ffile.close() #Close the file
    
reform()