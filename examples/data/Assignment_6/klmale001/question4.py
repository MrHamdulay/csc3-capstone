#Assignment 6 Question 4
#21 April 2014
#Alexi Kalamoudacos, Grade Mark Count
def MarkCalc():
    TotalMarks=input('Enter a space-separated list of marks:\n')
    IndivMarks=TotalMarks.split(' ') #Initialising lists in order to add the given marks
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    for i in IndivMarks: #appending the marks to their correct lists
        if int(i)<50:
            a.append(i)
        elif 50<=int(i)<60:
            b.append(i)
        elif 60<=int(i)<70:
            c.append(i)
        elif 70<=int(i)<75:
            d.append(i)
        else:
            e.append(i)
    print('1 |'+len(e)*'X')
    print('2+|'+len(d)*'X')
    print('2-|'+len(c)*'X')
    print('3 |'+len(b)*'X')
    print('F |'+len(a)*'X')
if __name__=='__main__':
    MarkCalc()