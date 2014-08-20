"""This program takes a list of marks and sort them in different categories
Masilela Mduduzi
25 April 2014"""

marks = input("Enter a space-separated list of marks:\n")
#creating the main list "marl_list and a new list for every category
marks_list = marks.split(" ")
Fail=[]
third=[]
lower_2nd=[]
upper_2nd=[]
first=[]

for i in range(len(marks_list)):
    #for the first category
    if eval(marks_list[i])>=75:
        first.append(marks_list[i])#adding the number into the list first

    #for the upper second category 
    elif 70<= eval(marks_list[i]) <75:
        upper_2nd.append(marks_list[i])

    #for the lower second category
    elif 60<= eval(marks_list[i]):
        lower_2nd.append(marks_list[i])

    #for the third category
    elif 50<=eval(marks_list[i])<60:
        third.append(marks_list[i])
    #for the fail category
    elif eval(marks_list[i])<50:
        Fail.append(marks_list[i])
print("1 |"+"X"*len(first))        
print("2+|"+"X"*len(upper_2nd))        
print("2-|"+"X"*len(lower_2nd))        
print("3 |"+"X"*len(third))        
print("F |"+"X"*len(Fail))
