"""Justify a paragraph in an inputted line width
Dylan Lubbe
15 May 2014"""

file_in = input ("Enter the input filename:\n")
file_out = input ("Enter the output filename:\n")
width = input ("Enter the line width:\n")
lines = []
f = open (file_in, "r")
lines = f.readlines()
f.close
str_list = []
for strings in lines:
    str_list += (strings[:-1].split(" "))

counter = 0 
ref_list = []
new_list = []
for word in str_list:
    counter += len(word)
    if counter < int(width):
        new_list.append (word)
    else:
        ref_list.append (new_list)
        counter = 0 
        new_list = [word]
        counter = len(word)
        
ref_list.append (new_list)
last_str = ""
full_str = ""
names_all = ""
for i in range (len(ref_list)):
    for j in ref_list[i]:
        full_str += (j + " ")
    names_all += (full_str + "\n")
    full_str = ""

g = open (file_out, "w")        
print (names_all, file=g)
g.close()



            
            
            