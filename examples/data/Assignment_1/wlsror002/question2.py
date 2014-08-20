

def main():
    valid="true"   
    if hours>23 or hours<0:
        valid="false"
    
    if minutes>59 or minutes<0:
        valid="false"
    
    if seconds>59 or seconds<0:
        valid="false"
    
    if valid=="true":
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
        
hours= eval(input("Enter the hours:\n"))
minutes= eval(input("Enter the minutes:\n"))
seconds= eval(input("Enter the seconds:\n"))

main()

        
