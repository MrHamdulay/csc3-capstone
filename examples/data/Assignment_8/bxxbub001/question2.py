def check_double(s):
    if len(s) -1 >= 1:
        if s[0]==s[1]:
            return check_double(s[2:])+1
        else:
            return check_double(s[1:])
    else:
        return 0
    
string1 = input("Enter a message:\n")
print("Number of pairs:",check_double(string1))
