#Program that sorts marks into relevant category
#Cameron Collum
#24 April 2014
marks=input("Enter a space-separated list of marks:\n") # allows users to enter in marks
lisM=marks.split(" ") # creates a list with marks
countF=0
count3=0
countl2=0  # creates counters for occurence of each individual section of marks
countu2=0
count1=0
for i in lisM: # iterates through list of marks and assigns it to relevant category
          if eval(i)<50:
                    countF+=1
          elif 50<=eval(i)<60:
                    count3+=1
          elif 60<=eval(i)<70:
                    countl2+=1
          elif 70<=eval(i)<75:
                    countu2+=1
          elif 75<=eval(i):
                    count1+=1
print("1 |"+"X"*count1)
print("2+|"+"X"*countu2)
print("2-|"+"X"*countl2) # prints category and number of marks in that category represented by X
print("3 |"+"X"*count3)
print("F |"+"X"*countF)