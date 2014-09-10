
#Dhriven Hamlall

def get_integer(a):
    num = (input ("Enter "+a+":\n"))
    while not num.isdigit ():
        num = (input ("Enter "+a+":\n"))#testing for letters and 0r negative digits
    num=eval(num) # eval makes it a digit practically
    return num

def calc_factorial(a):
    answer = 1
    for i in range (a,1,-1):
        answer= answer * i
    return answer

# [hmldhr001]
# [question1.py]

#Dhriven Hamlall


def display():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    x=input("Enter your selection:\n") # User makes a choice
    x=x.upper() # input will be in capitals
    return x # returning capital input

def main():
    choice="" # empty string
    message="no message yet"
    fileNotFoundMessage="File not found"  #initialising

    while choice!="X": # while user did not try to exit using x
        choice=display() #will continue to show menu option
        if(choice=="E"):
            message=input("Enter the message:\n")
        elif(choice=="V"):
            print("The message is:",message)
        elif(choice=="L"):
            print("List of files: 42.txt, 1015.txt")
        elif(choice=="D"):

            fileName=input("Enter the filename:\n")
            if(fileName=="42.txt"):
                print("The meaning of life is blah blah blah ...")
            elif(fileName=="1015.txt"):
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else:
                print(fileNotFoundMessage) #basically if 42.txt or 1015.txt is not entered

    else:
        print("Goodbye!")

main()

# [hmldhr001]
# [question3.py]

# calculate number of k-permutations of n items
# bhavana harrilal
# 10 April 2014

from mymath import *

def main ():
   n = get_integer ("n")
   k = get_integer ("k")
   nfactorial = calc_factorial (n)
   nkfactorial = calc_factorial (n-k)
   print ("Number of permutations:", nfactorial // nkfactorial)

if __name__ == "__main__":
   main()


# [hmldhr001]
# [question4.py]


#Dhriven Hamlall

import math



def enter():
    function=input("Enter a function f(x):\n")
    function=function.lower()
    return function

#=====================================================================================================

def plot_graph():

    y_value_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    function=enter()
    function=function.replace("x","(x)")

    for i in range(-10,11):
        y_value_list[(i+10)]=round(eval(str(function.replace("x",str(i)))))



    for y in range(10,-11,-1):
        Display=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        if(y==0):
            for x in range(-10,11):
                if(y_value_list[(x+10)]==0):
                    Display[(x+10)]="o"
                elif x==0:
                    Display[(x+10)]="+"
                else:
                    Display[(x+10)]="-"
        else:
            for i in range(-10,11):
                if -10<=y_value_list[(i+10)]<=10:
                    if y_value_list[(i+10)]==y:
                        Display[(i+10)]="o"
                    elif Display[10]!="o":
                        Display[10]="|"

#===========================================================================================================

        for i in range(21):
            print(Display[i])
        print()



plot_graph()

# [hmldhr001]
# [question2.py]

#Dhriven Hamlall

money=[100,25,10,5,1] #1c, 5c, 10c, 25c, $1
position=[0,0,0,0,0]


#------------------------------------------------------------------------------------------------------------------
def Work_out_change():
    i=0
    cost=eval(input("Enter the cost (in cents):\n"))
    deposit=0
    while deposit<cost:
        amount=eval(input("Deposit a coin or note (in cents):\n"))
        deposit=deposit+amount


    change=deposit-cost
#------------------------------------------------------------------------------------------------------------------

    while(change!=0):
        while((change>=int(money[i]))): #money[0]=100
            change=change-int(money[i])
            position[i]=str(int(position[i])+1)
        i=i+1

#------------------------------------------------------------------------------------------------------------------------


def display():
    change=False
    for i in range(5):
        if(int(position[i])>0):
            change=True

    if(change):
        print("Your change is:")
        for i in range(5):

            if(int(position[i])>0 and i==0):
                print(position[i],"x","$1")

            elif(int(position[i])>0 and i==1):
                print(position[i],"x","25c")

            elif(int(position[i])>0 and i==2):
                print(position[i],"x","10c")

            elif(int(position[i])>0 and i==3):
                print(position[i],"x","5c")

            elif(int(position[i])>0 and i==4):
                print(position[i],"x","1c")

#-------------------------------------------------------------------------------------------------------------------------------
Work_out_change()
display()
