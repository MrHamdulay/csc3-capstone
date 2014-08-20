# program that takes in a list of marks (separated by spaces) and
# outputs a histogram representation of 
# the marks according to the mark categories at UCT:
# hendrik joosten
# 24/04/2014

#declare variable to handle the list of marks
marks = []

# populate the list
x = input("Enter a space-separated list of marks:\n")
marks = x.split(" ")

# convert elements from str to int
for i in range(len(marks)):
      marks[i] = eval(marks[i])
      
# counters
first = 0
upper_second = 0
lower_second = 0
third = 0
fail = 0

# classify each mark and atttribute counters
for j in range(len(marks)):
      if marks[j] >= 75:
            first+=1
      if 75 > marks[j] >= 70:
            upper_second+=1
      if 70 > marks[j] >= 60:
            lower_second+=1
      if 60 > marks[j] >= 50:
            third+=1
      if marks[j] < 50:
            fail+=1
            
# create array containing counters
groups = [first,upper_second,lower_second,third,fail]


# print the histogram
print("1 |"+"X"*groups[0])
print("2+|"+"X"*groups[1])
print("2-|"+"X"*groups[2])
print("3 |"+"X"*groups[3])
print("F |"+"X"*groups[4])

            
            

            