choice_input  = input("Enter the input filename:\n")
choice_output = input("Enter the output filename:\n")
input_file = open(choice_input, "r")
output_file = open(choice_output, "w")
width = eval(input("Enter the line width:\n"))
string = input_file.read()
x = string.splitlines(True)
string = "".join(x)

paragraphs = string.split("\n\n")
for i in range(len(paragraphs)):
    paragraphs[i] = paragraphs[i].replace("\n", " ")

formatted_paragraphs = []
for para in paragraphs:
    para = para.split(" ")
    new_string = []
    count = 0
    
    for s in para: #s is each word in the current paragraph
        if count + int(len(s)) <= width:   #when the length of the new line is under the specified width, the string is just added to the list 
            new_string.append(s)
            new_string.append(" ")
            count+= int(len(s)+1)
        
        else:
            new_string.append("\n")  #when the length of the new line exceeds the specified with, a newline character is added then string is appended
            count = 0
            new_string.append(s)
            new_string.append(" ")
            count+= int(len(s)+1)
            
    formatted_paragraphs.append(new_string)

for i in formatted_paragraphs:
    if i[-1] == " ":
        i[-1] = ""
    else:
        continue

for para in formatted_paragraphs:
    string = "".join(para)
    string = string + "\n"
    print(string, file=output_file)
    
    
input_file.close()
output_file.close()




