# [gvnmer006]
# [question1.py]

#GVNMER006
#2014-04-16

def display():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    x=input("Enter your selection:\n")
    x=x.upper()
    return x

def main():
    choice=""
    message="no message yet"
    file="File not found"
    while choice!="X":
        choice=display()
        if(choice=="E"):
            message=input("Enter the message:\n")
        elif(choice=="V"):
            print("The message is:",message)
        elif(choice=="L"):
            print("List of files: 42.txt, 1015.txt")
        elif(choice=="D"):

            fName=input("Enter the filename:\n")
            if(fName=="42.txt"):
                print("The meaning of life is blah blah blah ...")
            elif(fName=="1015.txt"):
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else:
                print(file)

    else:
        print("Goodbye!")

main()







# [gvnmer006]
# [question4.py]

import math

#displayList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
count1=0


def input1():
    func=input("Enter a function f(x):\n")
    func=func.lower()
    return func

def plot():

    yList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    func=input1()
    func=func.replace("x","(x)")
    for i in range(-10,11):
        x1=str(i)
        yList[(i+10)]=round(eval(str(func.replace("x",x1))))


    for y in range(10,-11,-1):
        displayList=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        if(y==0):
            for x in range(-10,11):
                if(yList[(x+10)]==0):
                    displayList[(x+10)]="o"
                elif x==0:
                    displayList[(x+10)]="+"
                else:
                    displayList[(x+10)]="-"
        else:
            for i in range(-10,11):
                    #if i==0:
                if -10<=yList[(i+10)]<=10:
                    if yList[(i+10)]==y:
                        displayList[(i+10)]="o"
                    elif displayList[10]!="o":
                        displayList[10]="|"
                    #displayList[10].replace("|","o")


        for i in range(21):
          print(displayList[i])
        print()



plot()

# [gvnmer006]
# [question2.py]

count=[0,0,0,0,0,0,0]
list=[500,200,100,50,20,10,5]
#GVNMER006
#2014-04-16
def vending():
    i=0
    cost=input("Enter the cost (in cents):\n")
    cost=eval(cost)
    deposit=0
    while deposit<cost:
        amount=eval(input("Deposit a coin or note (in cents):\n"))
        deposit+=amount


    change=deposit-cost

    while(change!=0):
        while((change>=int(list[i]))):
            change=change-int(list[i])
            count[i]=str(int(count[i])+1)
        i+=1


def display():
    change=False
    for i in range(7):
        if(int(count[i])>0):
            change=True
    if(change):
        print("Your change is:")
        for i in range(7):
            if(int(count[i])>0 and i==0):
                print(count[i],"x","R5")
            elif(int(count[i])>0 and i==1):
                print(count[i],"x","R2")
            elif(int(count[i])>0 and i==2):
                print(count[i],"x","R1")
            elif(int(count[i])>0 and i==3):
                print(count[i],"x","50c")
            elif(int(count[i])>0 and i==4):
                print(count[i],"x","20c")
            elif(int(count[i])>0 and i==5):
                print(count[i],"x","10c")
            elif(int(count[i])>0 and i==6):
                print(count[i],"x","5c")
vending()
display()
