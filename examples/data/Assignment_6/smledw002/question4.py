#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 20 Apil 2014
#Function       : Draws a histogram of marks
#Title          : Question4

marks = list(map(eval, (input("Enter a space-separated list of marks:\n").split())))


first = "1 |"
upper_end = "2+|"
lower_end = "2-|"
third = "3 |"
fail = "F |"

for i in marks:

    if i >= 75:
        first += "X"
    elif i >= 70:
        upper_end += "X"
    elif i >= 60:
        lower_end += "X"
    elif i >= 50:
        third += "X"
    else:
        fail += "X"

print(first, upper_end, lower_end, third, fail, sep="\n")

