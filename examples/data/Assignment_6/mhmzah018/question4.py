"""Assignment 6 - question 4
Zaheer Mahmood
23-04-2014"""

#split the string into lists
given = input("Enter a space-separated list of marks:\n")
mark_sheet = given.split(" ")

#create variables to store counts
count_first = ""
count_u_second = ""
count_l_second = ""
count_third = ""
count_fail = ""

#create loop to allow count
for i in range (len(mark_sheet)):
    value = eval(mark_sheet[i])
    X="X"
    if value >= 75:
        count_first+=X
    elif value<75 and value>=70:
        count_u_second+=X
    elif value<70 and value>=60:
        count_l_second+=X
    elif value<60 and value>=50:
        count_third+=X
    else:
        count_fail+=X
#print output
print("1 |",count_first,sep="")
print("2+|",count_u_second,sep="")
print("2-|",count_l_second,sep="")
print("3 |",count_third,sep="")
print("F |",count_fail,sep="")


