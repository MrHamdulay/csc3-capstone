#Michael_Odhiambo
#ODHMIC003
#Assignment 6_Question 4
marks= input("Enter a space-separated list of marks:\n")# prompt user for input of marks
imp_marks= marks.replace(" ",",")#remove spaces inputed by user
x= imp_marks.split(",")


fail=[]
third=[]
lower=[]
upper=[]
first=[]
#loop used to scan through marks_list and organise and extract marks to populate lists of different values 
for i in x:
    if eval(i) < 50:
        fail.append(i)
    elif 50<=eval(i)<60:
        third.append(i)
    elif 60<=eval(i)<70:
        lower.append(i)
    elif 70<=eval(i)<75:
        upper.append(i)
    elif eval(i)>=75:
        first.append(i)
#print histogram
print('1 |','X'*len(first),sep="")
print('2+|','X'*len(upper),sep="")
print('2-|','X'*len(lower),sep="")
print('3 |','X'*len(third),sep="")
print('F |','X'*len(fail),sep="")        
    
