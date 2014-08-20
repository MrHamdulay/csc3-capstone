"""program that acts like a vending machine
   Rivoningo Seweya
   14 April 2014"""
# print initial statement

n=(eval(input("Enter the cost (in cents):\n")))

#create a loop the keeps track of the amount etered

i=0
while i<n:
    m=eval(input("Deposit a coin or note (in cents):\n"))
    i+=m
    
#create a method of determing the change that should be recieved by the person

change=i-n
if change>0:
    print("Your change is:")
    while change>0:
        c=0
        if change>=100:
            change1=change//100
            print(change1,"x $1")
            c+=(change1*100)
        elif 100>change>=25:
            change1=change//25
            print(change1,"x 25c")
            c+=(change1*25)               
        elif 25>change>=10:
            change1=change//10
            print(change1,"x 10c")
            c+=(change1*10)
        elif 10>change>=5:
            change1=change//5
            print(change1,"x 5c")
            c+=(change1*5)
        else:
            print(change,"x 1c")
            c+=(change*1)

        change-=c
      
            