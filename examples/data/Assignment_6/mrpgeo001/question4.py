"""Program to draw histogram from set of marks
Geoff Murphy
MRPGEO001
20 April 2014"""

marks = input("Enter a space-separated list of marks:\n")

marks_list = marks.split()    #Creates a list with the given values by splitting them into individual values

counter = [0 , 0 , 0 , 0, 0]  #The values which will determine the size of the respective bars(first value is 1, second is 2+, last is F)

#-------------------------------------------------------------------------------

for i in marks_list:          #Adds to the total size of the respective bars depending on the current value
    if eval(i) < 50:          #Turns the current value into an integer so comparison may be done
        counter[4] += 1
    elif 50 <= eval(i) < 60:
        counter[3] += 1
    elif 60 <= eval(i) < 70:
        counter[2] += 1
    elif 70 <= eval(i) < 75:
        counter[1] += 1
    else:
        counter[0] += 1
     
#-------------------------------------------------------------------------------
   
print("1 |", "X"*counter[0], sep = "")  #Prints the histogram, with 'X' being multiplied by the counter value for the particular value (e.g. 1, 2+ etc.)
print("2+|", "X"*counter[1], sep = "")
print("2-|", "X"*counter[2], sep = "")
print("3 |", "X"*counter[3], sep = "")
print("F |", "X"*counter[4], sep = "")

#-------------------------------------------------------------------------------