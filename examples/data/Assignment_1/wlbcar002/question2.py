hours = eval(input("Enter the hours:\n"))
if 0 <= hours <= 23 :
    caseA = True
else: caseA = False        
mins = eval(input("Enter the minutes:\n"))
if 0 <= mins <= 59 :
    caseB = True
else: caseB = False
secs = eval(input("Enter the seconds:\n"))
if 0 <= secs <= 59 :
    caseC = True
else: caseC = False
#print(hours, mins, secs)
if caseA==True & caseB==True & caseC==True :
    print("Your time is valid.")
else:
    print("Your time is invalid.")

