'''Program to create a histogram of marks
Tinotenda Chevmura (CHMTIN004)
20 April 2014'''

#_______________Program Starts Here_____________________________**

#create a list to store 5 counters with an initial value of 0

counter = [0, 0, 0, 0, 0]       # [1, 2+, 2-, 3, F]

#retrieve the string of marks from thhe user

marks = input("Enter a space-separated list of marks:\n")

# cartegorise each mark into their classes and start counting them

def mark_counter():
    for c in marks.split():
        if eval(c) >= 75:
            counter[0]+= 1
        elif 70<= eval(c) < 75:
            counter[1]+= 1
        elif 60 <= eval(c) < 70:
            counter[2]+= 1
        elif 50 <= eval(c) < 60:
            counter[3]+= 1
        elif 0 <= eval(c) < 50:
            counter[4]+= 1

# print the Histogram

def printHistrogram():
    print("1 |"+("X" * counter[0]))
    print("2+|"+("X" * counter[1]))
    print("2-|"+("X" * counter[2]))
    print("3 |"+("X" * counter[3]))
    print("F |"+("X" * counter[4]))
    
#call the functions to count the marks and print the histogram
mark_counter()
printHistrogram()

#_______________Program Ends Here_____________________________**