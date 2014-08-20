""" Students under the average standard deviation from a file
Dylan Lubbe
14 May 2014""" 

import math
# variables
lines = []
name_list = []
all_list = ""
names = []
marks = []
dev = 0
mark = 0
name = ""
total = 0
filename = input("Enter the marks filename:\n")
f = open (filename, "r")
lines = (f.readlines())
f.close
for words in lines:
 all_list = words.split(",")
 mark = (int(all_list[1]))
 total += mark 
 marks.append (mark)
 names.append (all_list)

mean = round(total/len(lines), 2) 

def std_dev (marks):
 sum2 = 0
 for x in marks:
  sum1 = (x-mean)**2
  sum2 += sum1
 dev = math.sqrt(sum2/len(marks))
 return dev

def stud_adv (names):
 for i in names:
  if int(i[1]) < mean-dev:
   name_list.append (i[0])
 return name_list

if __name__ == "__main__":
 stud_adv(names)
 print ("The average is:", "{0:0.2f}".format(mean))
 print ("The std deviation is:", "{0:0.2f}".format(std_dev(marks)))
 if name_list != []:
  print ("List of students who need to see an advisor:")
  for i in name_list:
   print(i)
  


   
 

