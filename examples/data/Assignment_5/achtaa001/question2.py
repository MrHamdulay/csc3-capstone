#Taahirah achmat
#ACHTAA001
#program to simulate a vending machine and calculate change based on the amount paid


d=input("Enter the cost (in cents):\n")
c=eval(d)

deposit=0
while deposit<c:
    amt=eval(input("Deposit a coin or note (in cents):\n"))
    deposit=deposit+amt
    
print("Your change is:")
if deposit==c:
    print("0")
if deposit>c:
    change=deposit-c
    doll=change//100
    twentyf=(change%100)//25
    ten=((change%100)%25)//10
    f=(((change%100)%25)%10)//5
    one=((((change%100)%25)%10)%5)//1
    
    if doll>0:
        print(doll, "x $1")
    if twentyf>0:
        print(twentyf, "x 25c")
    if ten>0:
        print(ten, "x 10c")
    if f>0:
        print(f, "x 5c")
    if one>0:
        print(one, "x 1c")