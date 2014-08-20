# Author : Rayaan Fakier FKRRAY001
# Date : 20 - 04 - 2014
# question4.py
'''Program that takes in a list of marks and outputs a histogram 
representation of the marks according to the mark categories'''

def main():
    marks = input("Enter a space-separated list of marks:\n")
    marks_list = marks.split() # Seperates each mark individually
    
    # Accumulator variables
    fails = 0
    thrds = 0
    scndslw = 0
    scndsup = 0
    frsts = 0
    
    # Places marks in their category
    for i in marks_list:
        val_mark = eval(i) # Turns marks str -> int
        if val_mark < 50:
            fails += 1
        elif 50 <= val_mark < 60:
            thrds += 1
        elif 60 <= val_mark < 70:
            scndslw += 1
        elif 70 <= val_mark < 75:
            scndsup += 1
        elif val_mark >= 75:
            frsts += 1
            
    # Prints histogram
    print("1 |" + "X" * frsts)
    print("2+|" + "X" * scndsup)
    print("2-|" + "X" * scndslw)
    print("3 |" + "X" * thrds)
    print("F |" + "X" * fails)
main()