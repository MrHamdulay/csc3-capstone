#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     19-03-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    message = input("Enter the message: \n")
    repeat = eval(input("Enter the message repeat count: \n"))
    thickness = eval(input("Enter the frame thickness: \n"))
    length = len(message)
    for i in range(thickness):
        print("|"*i + "+" + "-"*length + "-"*(thickness*2 - i*2) + "+" + "|"*i)
    for i in range(repeat):
        print("|"*thickness, message, "|"*thickness)
    for i in range(thickness):
        print("|"*(thickness-1-i) + "+" + "-"*length + "-"*((i+1)*2) + "+" + "|"*(thickness-1-i))

if __name__ == '__main__':
    main()
