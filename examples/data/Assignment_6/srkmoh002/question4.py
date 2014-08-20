# Najeeb Sirkhoth
# SRKMOH002
# question4.py
# Assignment 6 


# Create empty list    
marklist = []


#Get string from user
markstring = input("Enter a space-separated list of marks:\n")
for i in markstring.split():                        #split string               
    mark = eval(i)                                  #Convert literal to numerical
    marklist.append(mark)                           #Append numerical to list
     
    
    

fail=0
third=0
lowersecond=0
uppersecond=0
first=0
for i in marklist:                                 #Categorise marks
    if 0<=i<50:
        fail += 1
    elif 50<=i<60:
        third += 1
    elif 60<=i<70:
        lowersecond += 1
    elif 70<=i<75:
        uppersecond += 1
    else: 
        first += 1
        
print (("1 |")+(first)*("X"))                     
print (("2+|")+(uppersecond)*("X"))
print (("2-|")+(lowersecond)*("X"))
print (("3 |")+(third)*("X"))
print (("F |")+(fail)*("X"))

