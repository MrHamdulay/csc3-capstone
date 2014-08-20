"""mark histogram
Aaron Weinstein
23 April 2014"""

fails=0
thirds=0
lowerseconds=0
upperseconds=0
firsts=0

given=input("Enter a space-separated list of marks:\n")
marks=given.split(" ")
length=len(marks)

for n in range (length):
    if eval(marks[n])<50 and eval(marks[n])>=0:
        fails=fails+1
    elif eval(marks[n])<60 and eval(marks[n])>49:
        thirds=thirds+1
    elif eval(marks[n])<70 and eval(marks[n])>59:
        lowerseconds=lowerseconds+1
    elif eval(marks[n])<75 and eval(marks[n])>69:
        uperseconds=upperseconds+1
    else:
        firsts=firsts+1
print("1 |","X"*firsts,sep="")
print("2+|","X"*upperseconds,sep="")
print("2-|","X"*lowerseconds,sep="")
print("3 |","X"*thirds,sep="")
print("F |","X"*fails,sep="")