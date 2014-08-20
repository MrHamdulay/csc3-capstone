#Assignment 9
#Question 2
#Rabia Parker
#Due Date: 16/05/14

first_file = input("Enter the input filename:\n")
last_file = input("Enter the output filename:\n")
w = eval(input("Enter the line w:\n"))

opened = open(first_file, 'r')
read = opened.read()
opened.close()


strings = read.split("\n\n")
last = open(last_file, "w")
for a in strings:
    a = a.replace("\n"," ")
    a = a.split(" ") 
    amount=-1
    for wrd1 in a:
        amount+=len(wrd1)+1
        if amount <= w:
            print(wrd1,file=last,end= " ")
        else:
            print(file=last)
            print(wrd1,file=last,end=" ")
            amount = len(wrd1)
    print(file=last)
    print(file=last)
last.close()
    

