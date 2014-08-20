#A program that takes in a list of marks and outputs a histogram representation of the marks according to UCT mark categories
#Author: Michelle Njoroge
#25 April 2014

def marks():
    marks=input("Enter a space-separated list of marks:\n")
    marks=marks.split()
    
    countfail=0
    count3rd=0
    countlower2nd=0
    countupper2nd=0
    countfirst=0
    
    for mark in marks:
        if eval(mark)<50:
            countfail+=1
        elif 50<=eval(mark)<60:
            count3rd+=1
        elif 60<=eval(mark)<70:
            countlower2nd+=1
        elif 70<=eval(mark)<75:
            countupper2nd+=1
        else:
            countfirst+=1
           
    print("1"+" "+"|"+"X"*countfirst)
    print("2+"+"|"+"X"*countupper2nd)
    print("2-"+"|"+"X"*countlower2nd)
    print("3"+" "+"|"+"X"*count3rd)
    print("F"+" "+"|"+"X"*countfail)

marks()
