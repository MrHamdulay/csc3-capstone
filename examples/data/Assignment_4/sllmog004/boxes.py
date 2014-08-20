# Created by: Yaseen Sulliman 
# Assignment 4
# 4 April 2014

def print_square():
                for i in range(5):
                                if i==0 or i==4:
                                                print("*"*5)
                                else:
                                                print("*"+" "*3+"*")
def print_rectangle(width, height):
                for i in range(height):
                                if i==0 or i==height-1:
                                                print("*"*width)
                                else:
                                                print("*"+" "*(width-2)+"*")
def get_rectangle(width, height):
                s=''
                for i in range (1,height+1):
                                if i==1 or i==height:
                                                s = s +'*'*width +'\n'
                                else:
                                                s = s +'*' + (width -2)*' ' +'*'+'\n'
                return s
        