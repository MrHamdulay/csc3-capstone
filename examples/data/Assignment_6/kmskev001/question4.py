"""program to print a histogram showing marks according to mark categories
   kevin kumasamba
   23 april 2014"""

def marks():
    print("Enter a space-separated list of marks:")
    marks=input("")
    marks_list=marks.split(" ")
    return marks_list
 
m_list=[]   
for mark in marks():
    mark=eval(mark)
    m_list.append(mark)
    
# creating the different classes with conditions to print x's
# for each line - a changeable number of Xs must be saved
first=[]
upsecond=[]
losecond=[]
third=[]
fail=[]
for mark in m_list:
    if mark>=75:
        first.append("X")
    elif 70<=mark<75:
        upsecond.append("X")
    elif 60<=mark<70:
        losecond.append("X")
    elif 50<=mark<60:
        third.append("X")
    else:
        fail.append("X")
        
        
for i in range(1):
    print("1 |", end="")
    for x in first:
        print(x, end="")
        
for i in range(1):
    print("\n2+|", end="")
    for x in upsecond:
        print(x, end="")
        
for i in range(1):
    print("\n2-|", end="")
    for x in losecond:
        print(x, end="")
        
for i in range(1):
    print("\n3 |", end="")
    for x in third:
        print(x, end="")
        
for i in range(1):
    print("\nF |", end="")
    for x in fail:
        print(x, end="")
    print()