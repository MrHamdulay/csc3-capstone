# 12 May 2014
# program to determine who needs to see a career coucilor
# Tayla Radmore


file_name= input("Enter the marks filename: \n")
import math
final_list=[]
total=0
students_needing_councilling=[]
almost_standard_deviation=0

f = open (file_name, "r") 
all_lines=f.readlines() 
number_of_rows=len(all_lines)
f.close ()

for i in range(0,number_of_rows):
 
 current_line=all_lines[i]
 list_of_current_line=current_line.split(",")
 mark_ending=list_of_current_line[1]
 length=len(mark_ending)
 if mark_ending[length-1:length+1]=="\n":
  mark_ending=mark_ending[:length-1]
 list_of_current_line[1]=mark_ending
 final_list.append(list_of_current_line)
 
for i in range(0,number_of_rows):
 mark=final_list[i][1]
 total+=eval(mark)
 
average=total/number_of_rows

for i in range (0,number_of_rows):
 mark=final_list[i][1]
 working=(eval(mark)-average)*(eval(mark)-average)
 almost_standard_deviation+=working


even_closer_standard_deviation=almost_standard_deviation/number_of_rows
standard_deviation=math.sqrt(even_closer_standard_deviation)

 
lower_limit=average-standard_deviation
upper_limit=average+ standard_deviation
 
for i in range (0,number_of_rows):
 mark=eval(final_list[i][1])
 if final_list[i][0]!="Harris":
  if mark<lower_limit or mark>upper_limit:
   students_needing_councilling.append(final_list[i][0])
 
  
  
x="{:0.2f}"

print("The average is:", x.format(average))
print("The std deviation is:", x.format((standard_deviation)))
if len(students_needing_councilling) >0:
 
 print("List of students who need to see an advisor:")
for i in students_needing_councilling:
    print(i)
