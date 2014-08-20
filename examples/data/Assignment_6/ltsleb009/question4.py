#-------------------------------------------------------------------------------
# Name:        question4
# Purpose:
#
# Author:      Taylor
#
# Created:     24/04/2014
# Copyright:   (c) Taylor 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    """Represents marks in the form of a Histogram according to the grades"""

    marks = input("Enter a space-separated list of marks:\n").split(" ")
    first, upper_second, lower_second, third, fail = 0, 0, 0, 0, 0 #assignment

    for i in marks: #iterate over the list one mark at a time

        percentage = eval(i)
        #check to see which category the percentage falls under
        #if category found, increment the total by 1
        if percentage >= 75:
            first += 1

        elif 70 <= percentage <75:
            upper_second += 1

        elif 60 <= percentage < 70:
            lower_second += 1

        elif 50 <= percentage < 60:
            third += 1

        else:
            fail += 1
    #check the number of people in each category and print the result
    if first:
        print("1 |"+first*"X")

    elif first == False:
        print("1 |")

    if upper_second:
        print("2+|"+upper_second*"X")

    elif upper_second == False:
        print("2+|")

    if lower_second:
        print("2-|"+lower_second*"X")

    elif lower_second == False:
        print("2-|")

    if third:
        print("3 |"+third*"X")

    elif third == False:
        print("3 |")

    if fail:
        print("F |"+fail*"X")
    elif fail == False:
        print("F |")

if __name__ == '__main__':
    main()
