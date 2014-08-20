"""" histogram of marks
kenneth mphele
23/04/2014"""

def histogram():
    #inputs the marks
    marks=input("Enter a space-separated list of marks:\n")
    marks_split=marks.split()
    #this are list that stores different marks according to their rating
    fail=[]
    third=[]
    lower=[]
    higher=[]
    first=[]
    # takes each and every mark and puts them in their right range
    for mark in marks_split:
        mark=int(mark)
        if mark<50:
            fail.append(mark)
        elif mark<60:
            third.append(mark)
        elif mark<70:
            lower.append(mark)
        elif mark<75:
            higher.append(mark)
        elif mark<=100:
            first.append(mark)
        else:print("")
        
    print("1 |"+"X"*len(first))
    print("2+|"+"X"*len(higher))
    print("2-|"+"X"*len(lower))
    print("3 |"+"X"*len(third))
    print("F |"+"X"*len(fail))
histogram()
    