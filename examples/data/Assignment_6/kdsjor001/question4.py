"""Assignment 6 Question 4
21 April 2014
Jordan Kadish, Grade Mark Count"""
def MarkCalc():
    TotMarks=input('Enter a space-separated list of marks:\n')
    IndivMarks=TotMarks.split(' ') #Initialising lists in order to add the given marks
    Fail=[]
    Thir=[]
    LowSec=[]
    UpSec=[]
    Fir=[]
    for i in IndivMarks: #appending the marks to their correct lists
        if int(i)<50:
            Fail.append(i)
        elif 50<=int(i)<60:
            Thir.append(i)
        elif 60<=int(i)<70:
            LowSec.append(i)
        elif 70<=int(i)<75:
            UpSec.append(i)
        else:
            Fir.append(i)
    print('1 |'+len(Fir)*'X')
    print('2+|'+len(UpSec)*'X')
    print('2-|'+len(LowSec)*'X')
    print('3 |'+len(Thir)*'X')
    print('F |'+len(Fail)*'X')
if __name__=='__main__':
    MarkCalc()