# program to reformat textfile so that lines are atmost a given length
# by Jacob Mwanza
# 13/05/2014

# edit lines of file
def edit_line(lines,width):
   count = 0
   new_line = ''
   for word in lines:
      if word == '\n':
         new_line = (new_line + word + '\n')
         count = 0
      elif count+len(word)+1 == width:
         new_line = (new_line + word + '  ' + '\n')
         count = 0
      elif count+len(word) < width:
         new_line = (new_line + word + ' ')
         count = count + len(word) + 1
      elif count+len(word) == width:
         new_line = (new_line + word + ' \n')
         count = 0
      elif count+len(word) > width:
         new_line = (new_line + '\n' + word + ' ')
         count = 0 + len(word) + 1
   temp = new_line.split('\n')
   new_line = ''
   for i in range(len(temp)):
      if i == len(temp)-1:
         new_line = (new_line + temp[i][:-1])
      else:
         new_line = (new_line + temp[i][:-1] + '\n')
   return new_line


# read file contents
def readfile(filename):
   f = open (filename, "r")
   newlines = f.readlines()
   f.close ()
   words= []
   
   for i in range (len(newlines)-1):
      newlines[i] = newlines[i][:-1]
   for j in range(len(newlines)):
      if newlines[j] == '':
         newlines[j] = '#'
   for k in range (len(newlines)):
      temp = newlines[k].split(' ')
      for s in range(len(temp)):
         if temp[s] == '#':
            words.append('\n')
         else:
            words.append(temp[s])
            
   return words

# print new lines to new file
def print_file(in_file,out_file):
   f = open (out_file, "w")
   print(in_file, file = f, end='')
   f.close ()    

def file():
    
    # enter file from which to get input
   file_in = input('Enter the input filename:\n')
    
    # enter file from which to transfer edited input
   file_out = input('Enter the output filename:\n')
    
    # enter width of lines
   width = eval(input('Enter the line width:\n'))
    
   words = readfile(file_in) 
   editedlines = edit_line(words,width)
   print_file(editedlines,file_out)

file()