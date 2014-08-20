"""Program to sort marks
Runako Muzwidzwa
23/04/2014"""

marks=input("Enter a space-separated list of marks:\n")
fail=0
third=0
lower_snd=0
upper_snd=0
first=0
#split the marks
split_marks=marks.split()
#group the marks
for mark in split_marks:
    if int(mark)<50:
        fail+=1
    elif 50<= int(mark)<60:
        third+=1
    elif 60<= int(mark)<70:
        lower_snd+=1
    elif 70<= int(mark)<75:
        upper_snd+=1
    elif int(mark)>=75:
        first+=1
print("1 |","X"*first,sep="")
print("2+|","X"*upper_snd,sep="")
print("2-|","X"*lower_snd,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fail,sep="")