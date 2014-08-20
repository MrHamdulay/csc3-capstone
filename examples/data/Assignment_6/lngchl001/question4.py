#program that takes in marks and creates a histogram representation
#by Chloe Longmore
# 24 April 2014


def collect_data():
    #asks for input marks
    marks=input("Enter a space-separated list of marks:\n")
    marks= map(int,marks.split())
    marks_list=[]
    #adds split marks into list
    for i in marks:
        marks_list.append(i)
    fail=0
    third=0
    lwr_scnd=0
    upr_scnd=0
    first=0  
    #sorts marks into categories
    for i in marks_list:
        if i<50:
            fail+=1
        elif 50<=i<60:
            third+=1
        elif 60<=i<70:
            lwr_scnd+=1
        elif 70<=i<75:
            upr_scnd+=1
        else:
            first+=1
    #prints histogram of marks
    print("1 |","X"*first,sep='')
    print("2+|","X"*upr_scnd,sep='')
    print("2-|","X"*lwr_scnd,sep='')
    print("3 |","X"*third,sep='')
    print("F |","X"*fail,sep='')    

#calls function  
collect_data()