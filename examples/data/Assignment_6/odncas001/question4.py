"""histogram representation of a given list of marks
casey o'donnell
22 april 2014"""

marklist=input("Enter a space-separated list of marks:\n").split(" ")
hist=[['1',0],['2+',0],['2-',0],['3',0],['F',0]]
for i in marklist:
    if eval(i)<50:
        hist[4][1]+=1
    elif eval(i)<60:
        hist[3][1]+=1
    elif eval(i)<70:
        hist[2][1]+=1
    elif eval(i)<75:
        hist[1][1]+=1
    else:
        hist[0][1]+=1

a="{0:<2}|"
for i in range(len(hist)):
    print(a.format(hist[i][0]),"X"*hist[i][1],sep="")
    