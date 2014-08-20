"""
reneshan naidoo
ndxren013
15-05-2014
"""

choice_in  = input("Enter the input filename:\n")
choice_out = input("Enter the output filename:\n") #input
input_f = open(choice_in, "r")
output_f = open(choice_out, "w")
width = eval(input("Enter the line width:\n")) #input
string = input_f.read()
x = string.splitlines(True) #spliting with the newline character
string = "".join(x)

paragraphs = string.split("\n\n")
for i in range(len(paragraphs)):
    paragraphs[i] = paragraphs[i].replace("\n", " ")

formatted_paragraphs = []
for para in paragraphs:
    para = para.split(" ") #spliting on the space character
    new_string = []
    count = 0
    
    for s in para: #s is each word 
        if count + int(len(s)) <= width:   
            new_string.append(s) #adding to the created array
            new_string.append(" ")
            count+= int(len(s)+1)
        
        else:
            new_string.append("\n")  
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
    print(string, file=output_f)
    
    
input_f.close()
output_f.close()




