"""program to take in a list of marks and output a histogram representation
joshua gullan
22 april 2014"""

#get list of marks
mark_list=input("Enter a space-separated list of marks:\n")

#create a list for evaluated marks
marks=[]

#split mark_list into a list of strings
marks=mark_list.split()

#evaluate list of strings
marks=list(map(eval, marks))

#create variables for mark categories
group_1=0
group_2_plus=0
group_2_minus=0
group_3=0
group_fail=0

#run through list of marks and add each to corresponding mark category
for i in marks:
    if i>=75:
        group_1 +=1
    elif 70<=i<75:
        group_2_plus +=1
    elif 60<=i<70:
        group_2_minus +=1
    elif 50<=i<60:
        group_3 +=1
    elif i<50:
        group_fail +=1

#print out histogram
print("1 |", "X"*group_1, sep="")
print("2+|", "X"*group_2_plus, sep="")
print("2-|", "X"*group_2_minus, sep="")    
print("3 |", "X"*group_3, sep="")        
print("F |", "X"*group_fail, sep="")


