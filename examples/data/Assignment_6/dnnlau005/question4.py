"""draw histogram of inputted marks according to mark categories at UCT
Lauren Denny
24 April 2014"""

#get a list of marks
marks=input("Enter a space-separated list of marks:\n")
mark_list=marks.split()

#2-D array of corresponding "mark category"-"number of marks in category" pairs
counters=[["1 ",0],["2+",0],["2-",0],["3 ",0],["F ",0]]

#count number of marks in each category and update value in "counters"
for mark in mark_list:
    mark=eval(mark) # convert string from input to an number
    if mark<50:          #F
        counters[4][1]+=1 
    elif mark<60:        #3
        counters[3][1]+=1
    elif mark<70:        #2-
        counters[2][1]+=1
    elif mark<75:        #2+
        counters[1][1]+=1
    else:                #1
        counters[0][1]+=1

# draw histogram
for i in range(5):
    print(counters[i][0], "|","X"*counters[i][1],sep="") 
    #print category, "|", bar of X's to represent number of marks in category