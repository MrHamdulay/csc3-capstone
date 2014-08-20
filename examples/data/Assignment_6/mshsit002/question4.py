
"""Sithembiso Mashinini 
2014/04/25
Drwas a hisotgram of marcks """


user_input=input('Enter a space-separated list of marks:\n')
overall_marks=[]#empty list to store the data 
first_class=[]
second_class=[]
third_class=[]
fourth_class=[]
woodenspoons=[]
for i in user_input.split():#conditions given from the question
    overall_marks.append(int(i))
    if int(i)>=75:#sorting the the marks according to categorry 
        first_class.append(overall_marks)
    elif int(i)>=70:
        second_class.append(overall_marks)
    elif int(i)>=60:
        third_class.append(overall_marks)
    elif int(i)>=50:
        fourth_class.append(overall_marks)
    else:
        woodenspoons.append(overall_marks)
a=len(first_class)#finding the length of the length of number of marks in list the multiplying to string X
b=len(second_class)
c=len(third_class)
d=len(fourth_class)
e=len(woodenspoons)

#print(a)
#print(b)
#print(c)
#print(d)
#print(e)
print('1 '+'|'+a*'X')
print('2+'+'|'+b*'X')
print('2-'+'|'+c*'X')
print('3 '+'|'+d*'X')
print('F '+'|'+e*'X')