"""Categorising marks
Christopher Sterley
20/04/2014"""

#create variable for categories
category_list=["1 ","2+","2-","3 ","F "]

#create variable to store marks
marks_list=input("Enter a space-separated list of marks:\n")
marks_list=marks_list.split()

#create counter variables
fail=0
third=0
lower_second=0
upper_second=0
first=0

#count the number of marks in each category
for i in range(len(marks_list)):
    if int(marks_list[i])<50:
        fail+=1
    elif int(marks_list[i])<60:
        third+=1
    elif int(marks_list[i])<70:
        lower_second+=1
    elif int(marks_list[i])<75:
        upper_second+=1
    else:
        first+=1

#create list of number of marks in each category
marks_number_list=[]
marks_number_list.append(first)
marks_number_list.append(upper_second)
marks_number_list.append(lower_second)
marks_number_list.append(third)
marks_number_list.append(fail)

#print histogram
for j in range(len(category_list)):
    print(category_list[j],"|","X"*marks_number_list[j],sep="")