#------------------------------------------------------------------------------#
# A program that takes in a list of marks (separated by spaces) and outputs    #
# a histogram representation of the marks.                                     #
# Name: Thubelihle Mdlalose                                                    #
# Student Number: MDLTHU011                                                    #
#------------------------------------------------------------------------------#

def main():
    # Prompt the user to enter marks.
    marks = input("Enter a space-separated list of marks:\n")
    marks = marks.split()   # Split the marks and assign them to a list.

    # Converts the list of str into numeric values.
    x = []
    for i in marks:
        b = eval(i)
        x.append(b)
    
    # Draw the historigram.    
    A = 0
    B = 0
    C = 0
    D = 0
    F = 0
    for j in x:
        if j >= 75:
            A += 1
        elif j >= 70 and j < 75:
            B += 1
        elif j >= 60 and j < 70:
            C += 1
        elif j >= 50 and j < 60:
            D += 1
        else:
            F += 1
        
    # Display output.
    print("1 |", "X" * A, sep="")
    print("2+|", "X" * B, sep="")
    print("2-|", "X" * C, sep="")
    print("3 |", "X" * D, sep="")
    print("F |", "X" * F, sep="")
    
# Call the main function
main()    
