# a program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
# mashau zwivhuya
# 21 april 2014
def main():
    #getting input
    marks_input=input("Enter a space-separated list of marks:\n")
    # splitting the marks in list
    marks=marks_input.split(" ")
    # setting my initial count to 0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    #looping trhough the marks and adding them to my list
    for i in marks:
        num=eval(i)
        if num>=75:
            count1+=1
        elif 70<=num<75:
            count2+=1
        elif 60<=num<70:
            count3+=1
        elif 50<=num<60:
            count4+=1
        else :
            count5+=1
    #printing the output        
    print("1 |","X"*count1,sep="")
    print("2+|","X"*count2,sep="")
    print("2-|","X"*count3,sep="")
    print("3 |","X"*count4,sep="")
    print("F |","X"*count5,sep="")
    
main()    