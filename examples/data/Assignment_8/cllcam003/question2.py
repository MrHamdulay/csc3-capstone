# Cameron Collum
# counts number of pairs of letters repeated next to each other
# 05/08/2014

def count_pairs(s):
    if len(s) == 1:
        return 0
    elif len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    elif s[0] == s[1]:
        return 1 + count_pairs(s[2:])
    else:
        return count_pairs(s[1:])


string = input("Enter a message:\n")
print("Number of pairs: "+ str(count_pairs(string)))