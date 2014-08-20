"""Program to reformat text files
MRPGEO001
Geoff Murphy
16 May 2014"""

name = input("Enter the input file name:\n")
new_file_name = input("Enter the output file name:\n")
width = eval(input("Enter the line width:\n"))

#-------------------------------------------------------------------------------

f = open(name,'r')          #Opens the specified file
lines = f.read()            #Takes the file and makes it one string
f.close()
print(lines)
lines_list_0 = lines.split(' ')  #Splits the string into a list with words as single values
lines_list = []                  #A new list which will mainly be used

for i in lines_list_0:
    if i != '':
        lines_list.append(i)     #Appends the values from first list to second as long as it isn't enmpty ('')
print(lines_list)
        
#-------------------------------------------------------------------------------

counter = 0

new_file = open(new_file_name, 'w') #The file which will be written to

for i in lines_list:
    if (len(i) + counter) <= width: #Prints the words in a single line so long as the line length...
        print(i, end = " ")         #...doesn't exceed the given line width
        print(i, file = new_file, end = " ") #Writes the words to the new file as well
        counter += (len(i) + 1)              #Adds word length and a space to counter, which keeps track of the length of the line
        
    elif (len(i) + counter) > width: #Prints the words to a new line if the line length will exceed the given width
        counter = 0                  #Resets the counter to 0 for the new line
        print("")
        print(i, end = " ")
        print("", file = new_file)
        print(i, file = new_file, end = " ") #Does the same for the file writing
        counter += (len(i) + 1)

new_file.close() #Closes the new file

#-------------------------------------------------------------------------------

