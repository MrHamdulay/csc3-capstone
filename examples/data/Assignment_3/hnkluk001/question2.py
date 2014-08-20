# Luke Henkeman
# HNKLUK001
# CSC1015F, Assignment 3, question 2
# 21 March 2014

def triangle():
    height = eval(input("Enter the height of the triangle:\n"))
    gap = height -1
    for i in range(1,height*2, 2):
        print(' '*gap,end='')
        print('*'*i)
        gap -= 1
    
triangle()