"""Sizwe sibiya
Sbysiz002: 21 Apr 2014
Histogram of marks"""

#asking userfor arks and craeting a list in descending order
Mark = input('Enter a space-separated list of marks:\n')
Marks = Mark.split(" ")
Marks.sort()
Marks.reverse()

#Craeting list to store the marks
First = []
Second_1st = []
Second_2nd = []
Third = []
Fail = []

# allocate the into list according to their ranges
for i in range(len(Marks)):
    if int(Marks[i])>= 75 :
        First.append(Marks[i])
    elif 70<= int(Marks[i]) < 75 :
            Second_1st.append(Marks[i])
    elif 60 <= int(Marks[i]) < 70  :
            Second_2nd.append(Marks[i])
    elif 50 <= int(Marks[i]) <60 :
            Third.append(Marks[i])
    elif int(Marks[i]) < 50  :
            Fail.append(Marks[i]) 
            

#creating a histogram of X according to the ranges and the n.o of apperances              
print('1',' ','|','X'*len(First),sep='')
print('2','+','|','X'*len(Second_1st),sep='')
print('2','-','|','X'*len(Second_2nd),sep='') 
print('3',' ','|','X'*len(Third),sep='')
print('F',' ','|','X'*len(Fail),sep='')          