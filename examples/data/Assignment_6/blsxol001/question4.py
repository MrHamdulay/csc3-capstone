def histogram():
    marks = input("Enter a space-separated list of marks:\n")
    marks = marks.split(' ')
    fail = []
    third= []
    usecond = []
    lsecond = []
    first =[]
    for mark in marks:
        mark = eval(mark)
        if 0<= mark < 50:
            fail.append(mark)
        elif 50<= mark <60:
            third.append(mark)
        elif 60 <= mark < 70:
            lsecond.append(mark)
        elif 70 <= mark <75:
            usecond.append(mark)
        elif mark>=75:
            first.append(mark)
    print('1 |','X'*len(first),sep='')
    print("2+|","X"*len(usecond),sep='')
    print("2-|","X"*len(lsecond),sep ='')
    print("3 |","X"*len(third),sep ='')
    print("F |","X"*len(fail),sep='')
histogram()