"""A program to format a text file so that all lines are at most a given length
by Jeremy Smith SMTJER002
15 May 2014"""

#receives the name of the input and output files and the required format length of each sentence
file_input = input("Enter the input filename:\n")
file_output = input("Enter the output filename:\n")
line_len = eval(input("Enter the line width:\n"))

#reads the input file and copies the contents to a string
f = open(file_input, "r")
text = f.read()
f.close()

text=text.replace('\n\n','*') #replaces the paragraph spaces with a star
text=text.replace('\n',' ') #replaces the new-line characters with a space
list_paragraph = text.split('*') #splits the string into a list with each paragraph a string in the list 

text_list=[] #an empty list to build the new formatted text in
for i in range(len(list_paragraph)):
    text = list_paragraph[i] #assigns each paragraph as a string to 'text' and formats the paragraph to the specified line length
    for j in range(len(text)//line_len):
        stop = line_len
        while text[stop] != " ":
            stop -= 1
        text_list.append(text[0:stop])
        text = text[stop+1:]
    if len(text) > line_len:
        stop = line_len
        while text[stop] != " ":
            stop -= 1
        text_list.append(text[0:stop])
        text = text[stop+1:]
        text_list.append(text+'\n')
    else:   
        text_list.append(text+'\n')

#writes the list of formated sentences to the output file
f = open(file_output, "w")
for line in text_list:
    print(line, file=f)
f.close()