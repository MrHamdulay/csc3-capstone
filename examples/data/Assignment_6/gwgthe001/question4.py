#Thembekani Gwegwana
#A program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
#April 2014


#Initialising counters
first=0
second_upper=0
second_lower=0
third=0
fail=0
marks=input('Enter a space-separated list of marks:\n') #Asking user for marks
mark_list=marks.split()
for marks in mark_list:
    marks=int(marks)
    if (marks)<50:
        fail+=1
    elif (50<=(marks)<60):
        third+=1
    elif (60<=marks<70) :
        second_lower+=1
    elif (70<=marks<75) :
        second_upper+=1
    else:
        first+=1
    #Printing the histogram of marks
print('1','|'+'X'*first)
print('2+'+'|'+'X'*second_upper)
print('2-'+'|'+'X'*second_lower)
print('3','|'+'X'*third)
print('F','|'+'X'*fail)