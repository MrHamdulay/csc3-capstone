#stephanie latchmanan
#Assignment 6 (draws histogram from a list of marks)
#20 April 2014

#Enter a list of marks
marks = input("Enter a space-separated list of marks:\n")

#seperates marks into a list according to spaces
marks_list=marks.split(" ")

#count occurrence of marks in each category
first,sec,lower_sec,third,fail=0,0,0,0,0
for i in marks_list:
    if eval(i) >= 75:
        first=first+1
    elif 75 > eval(i) >= 70 :
        sec=sec+1
    elif 70 > eval(i) >= 60 :
        lower_sec=lower_sec+1
    elif 60 > eval(i) >= 50 :
        third=third+1
    else:
        fail=fail+1

#print histogram and counters
print("1 |", "X"*first, sep="")
print("2+|", "X"*sec, sep="")
print("2-|", "X"*lower_sec, sep="")
print("3 |", "X"*third, sep="")
print("F |", "X"*fail, sep="")