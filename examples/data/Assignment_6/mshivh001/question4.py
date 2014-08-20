#maisha ivha
#24/04/2014
#Write a program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT:

def main():
    #asking for users marks
    x=input("Enter a space-separated list of marks:\n").split()
    #assing the frequncy of particula marks range to 0
    fail=0  
    third=0
    lower=0
    upper=0
    first=0
    #a loop that counts the occurance of marks in their respectative ranges
    for i in x:
        i=eval(i)
     
        if i<50:
            fail=fail+1# number of marks bellow 50
        elif 50<=i<60:
            third=third+1# number of marks between 50 and 60
        elif 60<=i<70:
            lower=lower+1#number of marks between 60 and 70
        elif 70<=i<75:#number of marks between 70 and 75
            upper=upper+1
        else:
            first=first+1# number of marks above 75
    #promt the program to print the graph
    print("1 |"+first*"X")
    print("2+|"+upper*"X")
    print("2-|"+lower*"X")
    print("3 |"+third*"X")
    print("F |"+fail*"X")
    
main()