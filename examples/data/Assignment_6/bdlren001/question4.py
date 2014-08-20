#  a program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT:
# Budeli Rendani
# BDLREN001
# 20/04/2014

def main():
    q=[] # Creating an empty list for marks less than 50
    w=[] # Creating an empty list for marks between 50 and 60
    e=[] # Creating an empty list for marks between 60 and 70
    r=[] # Creating an empty list for marks between 70 and 75
    t=[] # Creating an empty list for marks greater than 75
    x=input("Enter a space-separated list of marks:\n").split() # Obtaining the list of marks from the user
    for i in x: # Looping through the list of marks and placing the mark into the list of their category
        i=eval(i)
        if i<50:
            q.append(i)
        elif 50<=i<60:
            w.append(i)
        elif 60<=i<70:
            e.append(i)
        elif 70<=i<75:
            r.append(i)
        else:
            t.append(i)
    a=len(q) # Finding the number of marks in the list q
    s=len(w) # Finding the number of marks in the list w
    d=len(e) # Finding the number of marks in the list e
    f=len(r) # Finding the number of marks in the list r
    g=len(t) # Finding the number of marks in the list t
    v="X"
    print("1 |"+v*g) # Printing out crosses corresponding to the number of marks in the list
    print("2+|"+v*f) # Printing out crosses corresponding to the number of marks in the list
    print("2-|"+v*d) # Printing out crosses corresponding to the number of marks in the list
    print("3 |"+v*s) # Printing out crosses corresponding to the number of marks in the list
    print("F |"+v*a) # Printing out crosses corresponding to the number of marks in the list
main()