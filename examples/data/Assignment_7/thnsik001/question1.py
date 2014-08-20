"""Sikhulile Thenjwayo
Assignment 7 q1
01/05/2014"""

string_list = []
instring = ""
#user inputs strings
count =0
print("Enter strings (end with DONE):")
while instring != "DONE":
    instring = input()
    if not instring in string_list:
        string_list.append(instring)
        count+=1
else:
    del string_list[count-1]
#output unique list
print("\nUnique list:")
for i in string_list:
    print(i)