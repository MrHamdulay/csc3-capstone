"""This program creates hollow boxes of stars
Author :Masilela Mduduzi
04 APRIL 2014"""
def print_square ():
                print("*"*5)
                for i in range (3):
                                print("*"+" "*(3)+"*")
                print("*"*5)
                                
def print_rectangle (width, height):
                print("*"*width)
                for i in range (height -2):
                                print("*"+" "*(width - 2) + "*")
                print("*"*width)
                                
def get_rectangle (width, height):
                x="*" * width+'\n'
                for i in range (height - 2):
                                x+="*"+" "*(width - 2) +"*"+'\n'
                x+=("*" * width)
                                
        
                return x

