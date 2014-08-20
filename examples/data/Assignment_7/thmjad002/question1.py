"""Assignment 7, Question 1
JT
30-05-2014"""

def getlist():
    print("Enter strings (end with DONE):")
    lst = []
    s = str(input())
    while s != "DONE":
        lst.append(s)
        s = str(input())
    else:
        return lst
    
def newlst(l):
    print("\nUnique list:")
    check = []
    for i in l:
        if i not in check:
            print(i)
            check.append(i)
        else:
            continue
        
        
    
    
    
newlst(getlist())
    
        
    