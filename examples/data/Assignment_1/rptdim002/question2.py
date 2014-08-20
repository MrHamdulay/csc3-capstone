#Rptdim002
#Program to check the validity of time entered
def main():
    h=eval(input("Enter the hours:"'\n'))
    m=eval(input("Enter the minutes:"'\n'))
    s=eval(input("Enter the seconds:"'\n'))
    #to check it time input falls under intervals
    if (0<=h<=23) and (0<=m<=59) and (0<=s<=59):
        print("Your time is valid.")
    else:
        print("Your time is invalid.")

main()
    
       