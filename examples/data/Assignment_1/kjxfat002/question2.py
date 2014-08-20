def tim():
    hours=eval(input("Enter the hours:\n"))
    mins=eval(input("Enter the minutes:\n"))
    seconds=eval(input("Enter the seconds:\n"))
    
    if hours>=0 and hours<=23 and mins>=0 and mins<=59 and seconds>=0 and seconds<=59  :
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
     
tim() 