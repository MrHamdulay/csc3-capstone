#  a program to check the validity of a time entered by the user as a set of three integers.
# BADUGELA MULISA
def main():
    hours = eval(input("Enter the hours:\n"))
    minutes = eval(input("Enter the minutes:\n"))
    seconds = eval(input("Enter the seconds:\n"))
    if 0<=hours<=23 and 0<=minutes<=59 and 0<=seconds<=59:
        print("Your time is valid.")
   
    else: 
        print("Your time is invalid.") # for any value of hour,minutes and seconds
        

main()