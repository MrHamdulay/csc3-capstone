# Luke Henkeman
# HNKLUK001
# CSC1015F, Assignment 3, question 1
# 21 March 2014

def rectangle():
    height = eval(input("Enter the height of the rectangle:\n"))
    width = eval(input("Enter the width of the rectangle:\n"))
    for i in range(1,height+1):
        print(width*'*')

rectangle()