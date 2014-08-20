# Cameron Collum 
# Adjusting width program
# 15/05/2014

input_file  = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
input_file = open(input_file, "r")
output_file = open(output_file, "w")
width = eval(input("Enter the line width:\n"))
string = input_file.read()
x = string.splitlines(True)
string = "".join(x)

passages = string.split("\n\n")
for i in range(len(passages)):
    passages[i] = passages[i].replace("\n", " ")

formatted_passages = []
for para in passages:
    para = para.split(" ")
    new_string = []
    count = 0
    
    for s in para: # each individual word 
        if count + int(len(s)) <= width:   # when the length of the new line is under the specified width it adds it
            new_string.append(s)
            new_string.append(" ")
            count+= int(len(s)+1)
        
        else:
            new_string.append("\n")  #when the length of the new line exceeds the specified with new line is appended
            count = 0
            new_string.append(s)
            new_string.append(" ")
            count+= int(len(s)+1)
            
    formatted_passages.append(new_string)

for i in formatted_passages:
    if i[-1] == " ":
        i[-1] = ""
    else:
        continue

for para in formatted_passages:
    string = "".join(para)
    string = string + "\n"
    print(string, file=output_file)
    
    
input_file.close()
output_file.close()




