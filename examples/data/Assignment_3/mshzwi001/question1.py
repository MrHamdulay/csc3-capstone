# a program to draw a rectangle of a given height and width using the ‘*’ character.
# mashau zwivhuya
# 20 march 2014
def main():
    fin=eval(input("Enter the height of the rectangle:\n"))
    fon=eval(input("Enter the width of the rectangle:\n"))
    for i in range(fin):
        print("*"*fon)
main()
