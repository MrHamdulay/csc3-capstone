'''program to reformat a file and save it to another file
Othniel KONAN
KNNOTH001
10 May 2014'''

from textwrap import wrap

#VARIABLE
content = []
text_2 = []
i=0

#SPLT A STRING ACCORDING TO A GIVEN WIDHT
def form(init,final,lt):
    '''plit a string according to a given widht and do not break up words'''
    global width
    global content
    global i    
    l=lt[init:final+1]                      #take the string containing a following character 
    if len(l) > 0 and i+width<=len(lt):     #establish condtion to stop recursion
        while l[-1] != ' ':                 #if the following character is not a space (check if we are breaking up words)
            l=l[:-1]                        #reduce the string and check again
        content.append(l)                   #append the correct string to the content 
        i+=len(l)                           #i increases by the len of the correct string (we do that to keep track of were we are in the list) 
        return form(i,i+width,lt)           #we continue to split the list
    elif i+width>len(lt):                   #if the remaining part of the list is less than the width
        if lt[i:len(lt)] != '':             #we check if it contains somethings
            content.append(lt[i:len(lt)])   #append the remaining part



#PROMPT USER FOR PARAMETERS
inp = input('Enter the input filename:\n')
out = input('Enter the output filename:\n')
width = eval(input('Enter the line width:\n'))

#OPEN THE FIRST FILE 
with open(inp,'r') as file_1:
    lt = file_1.readlines()                 #copy what is in the file as text

#MAKE SPECIAL COPY OF THE TEXT WHEN EACH LINE IS A PARAGRAPH
for i in range(len(lt)):                      
    if lt[i] != '\n' and i != len(lt)-1:            #if not an empty line or the last line
        text_2.append(lt[i][:-1]+' ')               #replace the backspace by a space and copy that line 
    else:
        text_2.append(lt[i])                        #copy the line
text_2 = ''.join(text_2).split('\n')                #join the text and slpit it into pragraphs

#SEPARATE THE LINE 
for line in text_2:                         #go through all the lines in text_2
    i=0                                     #reset the variable because of the recursive function
    form(0,width,line)                      #call the function to separate the lines
    content.append('!@$%')                  #put a marker to separate paragraph  

    

#COPY THE MODIFIED TEXT TO THE DESIRED FILE
with open(out,'w') as file_2:   
    for line in content:               #go through each line of content
        if line != '!@$%':             #check for paragraphs
            print(line,file=file_2)    
        else:
            print(file=file_2)         #print empty line for paragraphs
