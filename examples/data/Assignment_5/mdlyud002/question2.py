# Yudhi Moodley
# Assignmnt 5 Question 2
# 14 April 2014
# Write a code function for a change calculator

# I'm a chaarou so I made this this so i could mise my change
def main():
    cents=eval(input("Enter the cost (in cents):\n"))
    sum=0
    while sum<cents:
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
        sum=sum+deposit
    one=0
    five=0
    ten=0
    twenty_five=0
    dollar=0
    d=sum-cents
    while d>0:
        if 100<=d:
            dollar=dollar+1 
            d=d-100
        elif 25<=d:
            twenty_five=twenty_five+1
            d=d-25
        elif 10<=d:
            ten=ten+1
            d=d-10            
        elif 5<=d:
            five=five+1
            d=d-5
        elif 1<=d:
            one=one+1
            d=d-1
    print("Your change is:")
    if dollar == 0 and ten==0 and twenty_five==0 and one==0 and five==0:
        print("Enter the cost (in cents):\n")
    if dollar>0:
        print(dollar ,"x $1")
    if twenty_five>0:
        print(twenty_five ,"x 25c")
    if ten>0:
        print(ten ,"x 10c")
    if five>0:
        print(five ,"x 5c")
    if one>0:
        print(one ,"x 1c")
    
main()  #studentlife
