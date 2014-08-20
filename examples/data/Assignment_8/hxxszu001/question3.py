# Annie
# 08 May 2014
def ecnrpt(a):
    if len(a) == 1:
        if a.islower():
            if a == 'z':
                return 'a'
            else:
                return chr(ord(a) + 1)
        else:
            return a
    else:
        return ecnrpt(a[0]) + ecnrpt(a[1:])

string = input("Enter a message:\n")
print("Encrypted message:")
print(ecnrpt(string))