#Shaaheen Sacoor SCRSHA001
#Program to find pairs of repeat letters in a string
# 8 may 2014


def Pairs(s):
    if s == '':
        return  0
    else:
        if len(s)>=2:
            if s[0] == s[1]:
                return 1 + Pairs(s[2:])
            else:
                return 0 + Pairs(s[1:])
        else:
            return 0
        
def main():
    s = input("Enter a message:\n")
    x = Pairs(s)
    print("Number of pairs:",x)
main()