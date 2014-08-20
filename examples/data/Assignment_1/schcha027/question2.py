hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))
if 0<=hours<=23:
    checkH=1
else:
    checkH=0
if 0<=minutes<=59:
    checkM=1
else:
    checkM=0
if 0<=seconds<=59:
    checkS=1
else:
    checkS=0    
#print("H: ",checkH , "  M: ",checkM , "  S: ",checkS )
if checkM==1 & checkH==1 & checkS==1:
    print("Your time is valid.")
else:
    print("Your time is invalid.")

