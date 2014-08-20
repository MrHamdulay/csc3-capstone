"""Question 4 - make histogram out of inputted marks
Jembe Moran
25 April 2014"""
marks=input("Enter a space-separated list of marks:\n") #get marks from user
marks=marks.split(" ")
first=0 #make counts for each result
up_sec=0
low_sec=0
third=0
fail=0
for i in range(len(marks)):
    pupil=eval(marks[i])
    if pupil<50:
        fail+=1
    elif pupil<60:
        third+=1
    elif pupil< 70:
        low_sec+=1
    elif pupil< 75:
        up_sec+=1
    elif pupil<=100:
        first+=1
print("1 |", "X"*first, sep="") #print out hardcoded axis, then bar (x times variable)
print("2+|", "X"*up_sec, sep="")
print("2-|", "X"*low_sec, sep="")
print("3 |", "X"*third, sep="")
print("F |", "X"*fail, sep="")

