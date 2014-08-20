
def main():
    x = input("Enter a space-separated list of marks:\n")
    
    marks = x.split()
    faL = 0
    trd = 0
    Low = 0
    upper = 0
    fst = 0
    
    for i in marks:
        if eval(i) < 50:
            faL += 1
        elif eval(i)<60:
            trd += 1
        elif eval(i)<70:
            Low +=  1
        elif eval(i)<75:
            upper += 1
        else:
            fst += 1
    print("1 |" + "X"*fst)
    print("2+|" + "X"*upper)
    print("2-|" + "X"*Low)
    print("3 |" + "X"*upper)
    print("F |" + "X"*faL)

main()
