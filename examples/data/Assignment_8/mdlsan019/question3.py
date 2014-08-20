
mssge=input("Enter a message:\n")

def lower_case(s):
    if s=='':
        return ''

    elif not 97<=ord(s[0])<=122:

        return s[0] + lower_case(s[1:])

    elif s[0]==" ":

        return " " + lower_case(s[1:])

    elif s[0]=="z":

        return "a" + lower_case(s[1:])

    else:
        return chr(ord(s[0])+1) + lower_case (s[1:])
x=lower_case(mssge)

print("Encrypted message:")
if mssge!='':
    print(x)
