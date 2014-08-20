"""program to simulate BBS machine for exchanging messages and files
Mick Perring
14 April 2014"""

def main ():
    y = "no message yet"
    end = True
    while end:
        print ("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        x = input ("Enter your selection: \n") # user makes choice of whick function of BBS machine to use
        x = x.lower()
        if x == "e": # enter message function
            y = input ("Enter the message:\n")
        elif x == "v": # view message function
            print ("The message is: ",y, sep = "")
        elif x == "l": # list files function
            print ("List of files: 42.txt, 1015.txt")
        elif x == "d": # choose/display file on system function
            f = input ("Enter the filename:\n")
            if f == "42.txt":
                print ("The meaning of life is blah blah blah ...")
            elif f == "1015.txt":
                print ("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print ("File not found")
        elif x == "x": # exit function
            end = False
            print ("Goodbye!")
        
main ()
