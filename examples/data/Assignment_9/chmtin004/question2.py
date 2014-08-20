'''Program to analyze marks and determine which student need to see the advisor
Tinotenda Chemvura
11 May 2014'''
from copy import deepcopy
#___________________________PROGRAM STARTS HERE_________________________________
#function to create a list of strings from the input file
def create_list():
    filename = input('Enter the input filename:\n')
    file = open(filename, 'r')
    words = file.readlines()
    file.close()
    #slice off the "\n" at the end of each line
    for i in range(len(words)-1):
        if words[i] != "\n":
            words[i] = words[i][:-1]
        #insert a marker to indicate end of paragraph
        else:
            words[i] = "***"    
    words2 = deepcopy(words)
    #create paragraphs with a whole para saved as one list inside a larger list
    parag = "" 
    for i in range(len(words2)):
        parag += words[i] + " "
    parag+= "***" #mark end of last paragr
    lis2 = ""
    new_out1 = []
    #merge each paragraph into one long string and create list with each item in it a seperate paragraph
    while len(parag) > 0:
        if parag[0:3] != "***":
            lis2 += parag[0]
            parag = parag[1:]
        else:
            new_out1.append(lis2)
            lis2 = ""
            parag = parag[3:]
    return new_out1

#create new list with each item a representing a line with the given width
#split the paragraph into a list,
#loop through the paragraphs, adding the 1st word and slicing it off until
#the 1st word is longer than the width of the line left, then add that line
#to the bigger list. insert the marker *** to indicate end of paragtaph
new_out1 = create_list()
filename2 = input('Enter the output filename:\n')
width = eval(input('Enter the line width:\n')) + 1
new_out2 = []
for i in new_out1:
    #check if the are any consecutive space characters, if there are, replace
    #second space character with an underscore to mark position of the extra space
    list_char = list(i)
    for j in range(len(list_char) - 1):
        if list_char[j] ==  ' ' and list_char[j] == list_char[j + 1]:
            list_char[j+1] = '_'
            break
    i = ''.join(list_char)
    i2 = i.split()
    width_left = width
    lis3 = []
    str1 = ''
    while len(i2) > 0:
        if len(i2[0]) < width_left:
            add = i2[0]
            #check if there are any underscore characters, if there are, replace
            #them with a space to account for the extra space in the original 
            #string
            if add[0] == '_':
                list_char2 = list(add)
                list_char2[0] = ' '
                add = ''.join(list_char2)
            str1 += add + " "            
            if len(i2) > 0:
                sub = len(i2[0]) + 1                        
                width_left -= sub
            i2 = i2[1:]
            
        else:
            #remove the last space at the end of the line
            if str1[-1] == " ":
                str1 = str1[:-1]
            new_out2.append(str1)
            width_left = width
            str1 = ""
    new_out2.append(str1[:-1])
    new_out2.append("***")

#funtion to print the lines to an output file
#remove the last marker '***' and replace is with the last line since the
#previous loop stopped before it could add the last line
#close the file
def print_to_file():
    new_out3 = new_out2[:-1]
    out = open(filename2, "w")        
    for i in new_out3:
        if i == "***":
            print("\n",end = "", file = out)
        else:
            print(i, file = out)
    out.close()
print_to_file()
#_____________________________END OF PROGRAM____________________________________