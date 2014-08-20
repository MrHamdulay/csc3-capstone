'''Sanele Mdlalose
   17 May 2014
   Question2,Assignment9
   Text Formatting'''

input_filename=input("Enter the input filename:\n")
output_filename=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

f_input=open(input_filename, 'r')
f_output=open(output_filename, 'w')

lines=f_input.readlines()

n_lines=[]
for line in lines:
 if line=="\n":
  n_lines.append(line)
 elif line[-1]=="\n":
  
  n_lines.append(line[:-1])
 else:
  n_lines.append(line)
n_lines=' '.join(n_lines)

while n_lines!='':
 s=n_lines[:width]
 space_pos=s[::-1].find(' ')
 end=s.find('\n')
 if s[-1]!=' ':
  if len(n_lines)>=width:
   if end>=0:
    s=s[:end+1]
    print(s,file=f_output)
    n_lines=n_lines[end+2:]
   
   elif n_lines[width]==" ":
    s=s[:width+1]
    print(s,file=f_output)
    n_lines=n_lines[width+1:]
    
   else:
    s=s[:width-space_pos]
    print(s,file=f_output)
    n_lines=n_lines[width-space_pos:]
  else:
   print(n_lines,file=f_output)
   n_lines=n_lines[len(n_lines):]
   
 else:
    print(s,file=f_output)
    n_lines=n_lines[width:]
    


    
f_input.close()
f_output.close()