#Annie Ho
#08 May 2014

def count_pairs(a):
    if len(a) == 1:
        return 0
    elif len(a) == 2:
        if a[0] == a[1]:
            return 1
        else:
            return 0
    elif a[0] == a[1]:
        return 1 + count_pairs(a[2:])
    else:
        return count_pairs(a[1:])


string = input("Enter a message:\n")
print("Number of pairs: "+ str(count_pairs(string)))