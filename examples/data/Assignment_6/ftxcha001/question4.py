#Chantel Foot
#Question 4, Assignment 6

marks_list=(input("Enter a space-separated list of marks:\n")) #get input from user
marks= marks_list.split(" ") #get list from user, then split so can work with each value

count_fail = 0 #start each count of mark at 0 
count_3rd = 0
count_lower2nd = 0
count_upper2nd = 0
count_1st = 0

for i in marks: #marks is the list split so each is a string that will interate through the loop
    x = eval(i) #need to eval as using numbers
    if 0<=x<50: #range of each mark, so if the input mark given is in this range then will add to counter
        count_fail+=1 #add to previous total, so accumulating a total for each range of marks
    elif 50<=x<60:
        count_3rd+=1
    elif 60<=x<70:
        count_lower2nd+=1
    elif 70<=x<75:
        count_upper2nd+=1
    elif 75<=x<=100:
        count_1st+=1
        
print("1 |", count_1st * "X",sep="") #got the number for each group (counter) so now multiply that by X to get the number of X's
print("2+|", count_upper2nd * "X",sep="")
print("2-|", count_lower2nd * "X",sep="")
print("3 |", count_3rd * "X",sep="")
print("F |", count_fail * "X",sep="")


      
        
        
    
        