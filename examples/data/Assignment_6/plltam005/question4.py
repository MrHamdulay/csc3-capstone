""" Displaying marks on histogram
Tameryn Pillay
23 April """

def main():
    # ask user for input
    initial_marks = input("Enter a space-separated list of marks:\n")
    marks = initial_marks.split()
    
    # grade the marks
    first = []
    upper_second = []
    lower_second = []
    third = []
    fail = []
    for i in range(len(marks)):
        if int(marks[i]) < 50:
            fail.append(marks[i])
        elif 50 <= int(marks[i]) < 60:
            third.append(marks[i])
        elif 60 <= int(marks[i]) < 70:
            lower_second.append(marks[i])
        elif 70 <= int(marks[i]) < 75:
            upper_second.append(marks[i])
        else:
            first.append(marks[i])
   
    # creating histogram
    print("1 ","|",len(first)*"X",sep='')
    print("2+","|",len(upper_second)*"X",sep='')
    print("2-","|",len(lower_second)*"X",sep='')
    print("3 ","|",len(third)*"X",sep='')
    print("F ","|",len(fail)*"X",sep='')
    
main()    