#Ariel Rubin
#RBNARI001
#23 April 2014
#program to show a list of marks in a histogram

#creates an array for all the marks
singlemark = []
#asks the user to enter marks
mark = input("Enter a space-separated list of marks:\n")
#counter varaibles created to be used later on in the prgram
count1 = 0
countlow = 0
countup = 0
count3 = 0
countf = 0

#splits the marks up and adds each mark into the array
singlemark = mark.split(" ") 

#for loop to check each mark individually in the array
for i in range (len(singlemark)):
    #if mark is greater than or equal to 75, counter variable goes up
    if eval(singlemark[i]) >= 75:
        count1 = count1 + 1
        #if mark is greater than or equal to 70 but less than 75, counter variable goes up
    elif eval(singlemark[i]) < 75 and eval(singlemark[i]) >= 70:
        countup = countup + 1
        #if mark is greater than or equal to 60 but less than 70, counter variable goes up
    elif eval(singlemark[i]) < 70 and eval(singlemark[i]) >= 60:
            countlow = countlow + 1 
        #if mark is greater than or equal to 50 but less than 60, counter variable goes up
    elif eval(singlemark[i]) < 60 and eval(singlemark[i]) >= 50:
                count3 = count3 + 1  
         #if mark is less than 50, counter variable goes up       
    elif eval(singlemark[i]) <50:
        countf = countf + 1
#prints out the marks in a histogram
print ("1 |",count1*"X",sep="")
print ("2+|",countup*"X",sep="")
print ("2-|",countlow*"X",sep="")
print ("3 |",count3*"X",sep="")
print ("F |",countf*"X",sep="")