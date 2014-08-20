"""table of given marks
ringo shima
25/04/14"""

def main():
    
    
    marks = input("Enter a space-separated list of marks:\n")
    list = marks.split()
    
    first = 0
    second = 0
    lSecond = 0
    third = 0
    fail = 0
    for i in list:
        y = eval(i)
        
        if y >= 75:
            first += 1
        elif y >=70:
            second += 1
        elif y >= 60:
            lSecond += 1
        elif y >= 50:
            third += 1
        elif y < 50:
            fail += 1
    print("1 |"+"X"*first)
    print("2+|"+"X"*second)
    print("2-|"+"X"*lSecond)
    print("3 |"+"X"*third)
    print("F |"+"X"*fail)
        
main()