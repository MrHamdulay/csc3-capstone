'''program to reformat text file - making it print out at certain width
Thabiso Beau
13 May 2014
Assignment 9: #question2.py'''
x = input('Enter the filename:\n')
y = input('Enter the filename:\n')
z = eval(input('Enter the line width:\n'))

def text_format():
   #part 1 - assignment statements
   S = []
   total = ''
   #part 2 - modifying the file for its length
   file_1 = open(x, 'r')
   a = file_1.readlines() #extracting lines from file
   #q = a.split() #split lines into list
   file_1.close()
   outfile = open(y, 'w')
  
   for i in a:
      
      A = i.split(" ")
      for u in A:
         if '\n' in A:
            A.remove('\n')
           
      S= S+A#concatenate lists to form sub-strings
   #print(S)
   for j in S:
      #print(j)
      if len(total) + len(j) <z:
         total += j + " "
      else:
         print(total, file = outfile) #writing input to file _ parameter within print statement
         total = j +' ' #since it exceeded 40, the next word will be the one that made it be >40
   print(total, file = outfile) #writing input to file _ parameter within print statement
   outfile.close()
text_format()