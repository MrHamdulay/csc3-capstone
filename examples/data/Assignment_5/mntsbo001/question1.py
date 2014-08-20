#Sbonelo Mntungwa
#Assignment 4 Question 1
#17 April 2014

def main():
        intro=("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        print(intro)    
        choose=input("Enter your selection:\n")
        choose=choose.lower()
        orig_mess="no message yet"
        file1='42.txt'
        file2='1015.txt'
        if choose == "x":
                        print("Goodbye!")        
        while choose != "x": 
                if choose =="e":
                        entr_mess=input("Enter the message:\n")
                        orig_mess=entr_mess
                elif choose =="v":
                        print("The message is:",orig_mess)
                elif choose == "l" :
                        print("List of files:",file1+",",file2)
                elif choose == "d":
                        opnfl=input("Enter the filename:\n")
                        if opnfl == file1:
                                file1 = 'The meaning of life is blah blah blah ...'
                                print(file1)
                        elif opnfl == file2:
                                file2 = 'Computer Science class notes ... simplified'+'\n'+'Do all work'+'\n'+'Pass course'+'\n'+'Be happy'
                                print(file2)
                        else:
                                print("File not found")
                print(intro)
                choose = input("Enter your selection:\n")
                choose = choose.lower()
        if choose == "x":
                print("Goodbye!")
        

main()