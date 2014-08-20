def counting(p):
    if len(p) == 1:
        return 0
    elif len(p) == 2:
        if p[0] == p[1]:
            return 1
        else:
            return 0
    elif p[0] == p[1]:
        return 1 + counting(p[2:])
    else:
        return counting(p[1:])


string = input("Enter a message:\n")
print("Number of pairs: "+ str(counting(string)))
