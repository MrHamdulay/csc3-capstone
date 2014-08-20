"""Question 4
Assignment 6
Micaela Menegaldo"""

def mark_histogram(marks):
    fail=""
    third=""
    lower_second=""
    upper_second=""
    first=""
    for i in marks:
        if int(i)<50:
            fail+="X"
        elif 50<=int(i)<60:
            third+="X"
        elif 60<=int(i)<70:
            lower_second+="X"
        elif 70<=int(i)<75:
            upper_second+="X"
        else:
            first+="X"
    print("1 |",first,sep='')
    print("2+|",upper_second,sep='')
    print("2-|",lower_second,sep='')
    print("3 |",third,sep='')
    print("F |",fail,sep='')
            


if __name__=='__main__':
    marks_list=(input("Enter a space-separated list of marks:\n")).split(" ")
    mark_histogram(marks_list)