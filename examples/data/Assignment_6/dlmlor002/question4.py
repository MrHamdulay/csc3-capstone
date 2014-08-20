"""program that makes a histogram of a list of marks
Lorena Dal Maso
24 April 2014"""

#create list of marks and mark variable
marks_list= input("Enter a space-separated list of marks:\n")
mark = marks_list.split(" ")
variable=[]
#categorise each mark according to UCT "symbols"
for i in mark:
    if eval(i)<50:
        grade="F"
    elif 50<=eval(i)<60:
        grade="3"
    elif 60<=eval(i)<70:
        grade="2-"
    elif 70<=eval(i)<75:
        grade="2+"
    elif 75<=eval(i):
        grade="1"
    #print(grade)
    if grade not in variable:
        variable.append(grade)
        
#initialise counters
countF=0
count3=0
count2_l=0
count2_u=0
count1=0

#count amount of which each "symbol" appears in marks_list
for i in mark:
    if eval(i)<50:
        countF= countF +1
    elif 50<=eval(i)<60:
        count3= count3 +1
    elif 60<=eval(i)<70:
        count2_l= count2_l +1
    elif 70<=eval(i)<75:
        count2_u= count2_u +1
    elif 75<=eval(i):
        count1= count1 +1
#print(countF,count3,count2_l,count2_u,count1)

print("1 |","X"*count1,"\n2+|","X"*count2_u,"\n2-|","X"*count2_l,"\n3 |","X"*count3,"\nF |","X"*countF,sep="")