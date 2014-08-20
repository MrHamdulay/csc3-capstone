"""Program to output a histogram representation of a list of marks
Tsanwani Vhonani
22 April 2014"""

def histo():
    
    #get the list from user
    marks=input("Enter a space-separated list of marks:\n").split()
    a=0
    b=0
    c=0
    d=0
    e=0
    
    first=""
    upper_second=""
    lower_second=""
    third=""
    fail=""
    
    for mark in marks:
        mark=int(mark)
        if mark>=75:
            a=a+1
            first=a*"X"
        if 70<=mark<75:
                b=b+1
                upper_second=b*"X"
        if 60<=mark<70:
                c=c+1
                lower_second=c*"X"
        if 50<=mark<60:
                d=d+1
                third=d*"X"
        if mark<50:
            e=e+1
            fail=e*"X"""
    print("1","|" + first) 
    print("2+"+"|"+upper_second)
    print("2-"+"|"+lower_second)
    print("3","|"+third) 
    print("F","|"+fail)
    
histo()