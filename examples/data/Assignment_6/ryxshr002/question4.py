"""shriya roy
23 April 2014
program to categorize marks"""


def main():
    #get input from user
    marks=input("Enter a space-separated list of marks:\n")
    #create a list of the marks
    marks_list=marks.split(" ")
    #create lists for each category of marks
    F=[]
    _3=[]
    two_lower=[]
    two_upper=[]
    first=[]
    #sort marks and append to lists
    for a in marks_list:
        b=int(a)
        if b<50:
            F.append(b)
        if 50<=b<60:
            _3.append(b)
        if 60<=b<70:
            two_lower.append(b)
        if 70<=b<75:
            two_upper.append(b)
        if b>=75:
            first.append(b)
    #count the number of items in each list
    num_1=len(F)
    num_2=len(two_upper)
    num_3=len(two_lower)
    num_4=len(_3)
    num_5=len(first)
    #print histogram
    print("1 |"+"X"*num_5)
    print("2+|"+"X"*num_2)
    print("2-|"+"X"*num_3)
    print("3 |"+"X"*num_4)
    print("F |"+"X"*num_1)
    
main()