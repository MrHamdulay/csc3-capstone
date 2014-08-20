#file loops
#Amo Motukisi
e="E" or "e"
l="L" or "l"
v="V" or "v"
d="D" or "d"
x="X" or "x"

a="Welcome to UCT BBS"
b="MENU"
c="(E)nter a message"
d="(V)iew message"
e="(L)ist files"
f="(D)isplay file"
g="e(X)it"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
selection=input("Enter your selection:\n")
message ="no message yet"

if selection=='E' or selection=='e':
    message =input("Enter the message:\n")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    selection=input("Enter your selection:\n")
if selection=='V' or selection=='v':
    print("The message is:", message)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    selection=input("Enter your selection:\n")

elif selection=='L' or selection=='l':
    print("List of files: 42.txt, 1015.txt")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    selection=input("Enter your selection:\n")
if selection=='D' or selection=='d':
    h=input("Enter the filename:\n")
    if h=='42.txt':
        text_file=open("42.txt", "w")
        lines = ["The meaning of life is blah blah blah..."]
        text_file.writelines(lines)
        text_file.close()
        
        text_file = open("42.txt", "r")
        data=text_file.read()
        print(data)
        #print(text_file.read())
        #text_file.close()
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        selection=input("Enter your selection:\n")
    elif h=='1015.txt':
        text_file=open("1015.txt", "w")
        
        text_file.write("computer Science class notes ... simplified\n")
        text_file.write("Do all work\n")
        text_file.write("Pass course\n")
        text_file.write("Be happy")
        text_file.close()
        
        text_file = open("1015.txt", "r")
        print(text_file.read())
        #text_file.close()
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        selection=input("Enter your selection:\n")
    elif h!='1015.txt' or h!='42.txt':
        print("File not found")
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        selection=input("Enter your selection:\n")

        
if selection=='X' or selection=='x':
    print("Goodbye!")
    

